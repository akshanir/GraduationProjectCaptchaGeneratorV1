import http.server
import socketserver
import generator
import time
import signal
#signal handler writing log info before shutting down the server. LOG.txt will contain analytical data for the server's last run
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


#to access the server:  http://127.0.0.1:10000/
PORT = 10000
RUN_TIME = time.time()
successfull_accesses = 0
total_attempts = 0
solution = ''

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global solution
        global total_attempts
        global successfull_accesses
        #get captcha on first run
        if total_attempts == 0:
            sol = generator.get_captcha_image()
            total_attempts+=1
            solution = sol
        else:
            sol = solution
        if self.path.find("input")!=-1:
            #checking the value of the user's input
            start = 8
            if self.path.find("index.html")!=-1:
                start += 10
            field=''
            for i in self.path[start:]:
                field+=i
            #comparing it with the captcha's solution
            if field == sol:
                successfull_accesses+=1
                total_attempts+=1
                solution = generator.get_captcha_image()
            else:
                solution = generator.get_captcha_image()
                total_attempts+=1
        #if user presses the captcha reset button
        elif self.path.find("click=true") !=-1 or self.path == "/out.png":
            solution = generator.get_captcha_image()
            total_attempts+=1
            #wait 0.6 seconds to wait for the new captcha image to be created and written on disk, otherwise the server might display the old image
            time.sleep(0.6)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)



signal.signal(signal.SIGINT, handler)
Handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()