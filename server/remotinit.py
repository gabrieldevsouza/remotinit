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
	elif str(item) == "Run server":
		os.system("start c:/bedrock-current/bedrock_server.exe")
	#elif str(item) == "Say Hello!":
	#	print("Hello, World!")
	#elif str(item) == "Subitem 1":
	#	print("Subitem 1")
	#elif str(item) == "Subitem 2":
	#	print("Subitem 2")
	
    
icon = pystray.Icon("RemotInit!", image, menu=pystray.Menu(
	pystray.MenuItem("Quit", on_click),
	pystray.MenuItem("Run server", on_click),
	#pystray.MenuItem("Say Hello!", on_click),
	#pystray.MenuItem("Submenu", pystray.Menu(
	#	pystray.MenuItem("Subitem 1", on_click),
	#	pystray.MenuItem("Subitem 2", on_click),
	#)),
))


class NeuralHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()

		self.wfile.write(bytes("<html><body><h1>Oi Jessica!</h1></body></html>", "utf-8"))
		return


	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type", "application/json")
		self.end_headers()


		content_len = int(self.headers.get('Content-Length'))
		post_body = self.rfile.read(content_len)
		print("Content:", post_body)
		return


server = HTTPServer((HOST, PORT), NeuralHTTP)
server.serve_forever()
server.serve_close()
print("Server started http://%s:%s" % (HOST, PORT))

#icon.run()


#