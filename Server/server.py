import http.server
import socketserver
import generator
#http://127.0.0.1:10000/
PORT = 10000
class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        sol = generator.get_captcha_image()
        self.path = self.path.replace('default.png',sol)
        #this part needs work
        if self.path.find("input"):
            field =""
            for i in self.path[8:]:
                if (i=='&'):
                    break
                field+=i
            if field == sol[:4]:
                print("correct..")
        #this one works
        if self.path.find("click=true") != -1:
            temp = sol
            sol = generator.get_captcha_image()
            self.path = self.path.replace(temp,sol)
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Http Server Serving at port", PORT)
    httpd.serve_forever()