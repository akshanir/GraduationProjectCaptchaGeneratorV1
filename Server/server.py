import http.server
import socketserver
import generator
import time
import signal
def handler(signum, frame):
    f = open('LOG.txt','w')
    total_time = round(time.time() - RUN_TIME)
    f.write(f"""total run time:    {total_time} seconds
total requests:    {total_attempts}
requests per second:    {round(total_attempts/total_time,4)}
requests per second without the hard coded latency:    {round(total_attempts/(total_time - total_attempts * (0.6)),4)}
successfull accesses:    {successfull_accesses}
successfull accesses per second:    {round(successfull_accesses/total_time,4)}
successfull accesses per second without the hard coded latency:    {round( successfull_accesses / (total_time - total_attempts * (0.6)),4)}""")
    f.close()
    print("server closed, written log on LOG.txt")
    exit(1)
    
#http://127.0.0.1:10000/
PORT = 10000
RUN_TIME = time.time()
successfull_accesses = 0
total_attempts = 0
solution = ''

signal.signal(signal.SIGINT, handler)
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global solution
        global total_attempts
        global successfull_accesses
        if total_attempts == 0:
            sol = generator.get_captcha_image()
            total_attempts+=1
            solution = sol
        else:
            sol = solution
        if self.path.find("input")!=-1:
            start = 8
            if self.path.find("index.html")!=-1:
                start += 10
            field=''
            for i in self.path[start:]:
                field+=i
            if field == sol:
                successfull_accesses+=1
                self.path = 'access.html'
            else:
                solution = generator.get_captcha_image()
                total_attempts+=1
        elif self.path.find("click=true") !=-1 or self.path == "/out.png":
            solution = generator.get_captcha_image()
            total_attempts+=1
            time.sleep(0.6)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()