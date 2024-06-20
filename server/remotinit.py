import os
import pystray
import PIL.Image
from http.server import HTTPServer, BaseHTTPRequestHandler

image = PIL.Image.open("icon.png")

HOST = "192.168.15.106"
PORT = 2011

def on_click(icon, item):
	if str(item) == "Quit":
		icon.stop()
	elif str(item) == "START server":
		server = HTTPServer((HOST, PORT), NeuralHTTP)
		server.serve_forever()
		server.serve_close()
		print("Server started http://%s:%s" % (HOST, PORT))
	
    
icon = pystray.Icon("RemotInit!", image, menu=pystray.Menu(
	pystray.MenuItem("Quit", on_click),
	pystray.MenuItem("START server", on_click),
	pystray.MenuItem("STOP server", on_click),
))

def check_message(message):
	if message == 'WAKEBEDROCK':
		os.system("start c:/bedrock-current/bedrock_server.exe")



class NeuralHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(bytes("<html><body><h1>Oi Jessica!</h1></body></html>", "utf-8"))
		return


	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "text/plain")
		self.end_headers()


		content_len = int(self.headers.get('Content-Length'))
		post_body = self.rfile.read(content_len)
		check_message(post_body.decode("utf-8"))
		return


icon.run()



#