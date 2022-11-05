import http.server
import socketserver
import generator
#http://127.0.0.1:10000/
PORT = 10000
succesful_accesses = 0
solution = ''
first_run = False

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global solution
        global succesful_accesses
        global first_run
        if not first_run:
            sol = generator.get_captcha_image()
            solution = sol
            first_run = True
        else:
            sol = solution
        if self.path.find("input")!=-1:
            field=''
            for i in self.path[8:]:
                field+=i
            if field == sol:
                #DON'T FORGET TO CHANGE
                succesful_accesses+=1
                self.path = 'access.html'
        if self.path.find("click=true") !=-1:
            self.path = self.path[0]
            solution = generator.get_captcha_image() 
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()