import http.server
import socketserver
import urllib.parse
port = 8080

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # key:str = '1'
        # if self.path == '/':
        #     file_path = f'./my_code/{key}/index.html'
        #     self.path = file_path
        # elif self.path == '/{key}':
        #     file_path = f'./my_code/{key}/index.html'
        #     self.path = file_path
        # try:
        #     return http.server.SimpleHTTPRequestHandler.do_GET(self)
        # except BrokenPipeError as e:
        #     print(e)         
        parsed_url = urllib.parse.urlparse(self.path)
        path_components = parsed_url.path.split('/')
        
        if len(path_components) >= 3 and path_components[2] == 'index.html':
            key_value = path_components[1]
            file_path = f'./files/{key_value}/index.html'
            self.path = file_path
        try:
            return http.server.SimpleHTTPRequestHandler.do_GET(self)  
        except BrokenPipeError as e:
            return e
with socketserver.TCPServer(("", port), MyRequestHandler) as server:
    print(f"Server started on port {port}")
    server.serve_forever()


