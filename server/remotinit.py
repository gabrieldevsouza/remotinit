import os
import threading
import time
import pystray
import PIL.Image
from http.server import HTTPServer, BaseHTTPRequestHandler

image = PIL.Image.open("icon.png")

print("")

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


HOST = "192.168.15.106"
PORT = 2011

server_started = False

server = HTTPServer((HOST, PORT), NeuralHTTP)

def start_server():
	global server_started
	global server
	print("BEGIN START server")
	server_started = True
	print("Server started on http://%s:%s" % (HOST, PORT))
	server.serve_forever()
	print("SERVER CLOSED")


def on_click(icon, item):
	global server_started
	if str(item) == "Quit":
		if server_started == True:
			server.shutdown()
			server_started = False

			print("Exiting...")
			time.sleep(2)

		icon.stop()
	elif str(item) == "START server":
		if server_started == False:
			threading.Thread(target=start_server, daemon=True).start()
		else:
			print("Server already started")
	elif str(item) == "STOP server":
		server.shutdown()
		server_started = False
		
	
    
icon = pystray.Icon("RemotInit!", image, menu=pystray.Menu(
	pystray.MenuItem("Quit", on_click),
	pystray.MenuItem("START server", on_click),
	pystray.MenuItem("STOP server", on_click),
))


def start_icon():
	print("BEGIN START icon")
	icon.run()

#


def main():
	print("BEGIN main")
	threading.Thread(target=start_server, daemon=True).start()
	threading.Thread(target=start_icon, daemon=True).start()
	
	while True:
		time.sleep(10000)

main()