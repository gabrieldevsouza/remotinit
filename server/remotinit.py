import os;
import threading;
import time;
import pystray;
import PIL.Image;
from http.server import HTTPServer, BaseHTTPRequestHandler;
import psutil;

image = PIL.Image.open("icon.png");

BEDROCK_PATH = "C:\\bedrock-current\\bedrock_server.exe";
BEDROCK_PROCESS = os.path.basename(os.path.normpath(BEDROCK_PATH));
#c:/bedrock-current/bedrock_server.exe

print("");

bedrock_starting = False;
listener_started = False;

def check_process(process_name):
	return process_name in (p.name() for p in psutil.process_iter());

def check_message(message):
	global bedrock_starting;
	if message == 'WAKEBEDROCK':
		request_start_bedrock();
		

def request_start_bedrock():
	if bedrock_starting == False:
		#threading.Thread(target=start_bedrock_process, daemon=True).start();
		print(check_bedrock_process());
	else:
		print("Bedrock already started");

def start_bedrock_process():
	print("")
	print("")
	print(" :: OPEN BEDROCK SERVER EXE :: ");
	print(os.popen("start "+BEDROCK_PATH).read());

	print("")
	print("")

	bedrock_starting = True;

	finish_bedrock_wait(10);

def check_bedrock_process():
	return check_process(BEDROCK_PROCESS);

def finish_bedrock_wait(wait_time):
	time.sleep(wait_time);
	bedrock_starting = False;

class NeuralHTTP(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200);
		self.send_header("Content-type", "text/html");
		self.end_headers();

		self.wfile.write(bytes("<html><body><h1>Oi Jessica!</h1></body></html>", "utf-8"));
		return


	def do_POST(self):
		self.send_response(200);
		self.send_header("Content-type", "text/plain");
		self.end_headers();


		content_len = int(self.headers.get('Content-Length'));
		post_body = self.rfile.read(content_len);
		check_message(post_body.decode("utf-8"));
		return


HOST = "192.168.15.106";
PORT = 2011;

def start_listener():
	global listener_started;
	global server;

	print("START server");

	listener_started = True;

	print("");
	print("");
	print("Server started on http://%s:%s" % (HOST, PORT));
	print("");
	print("");
	
	server.serve_forever();
	print("LISTENER CLOSED");


def on_click(icon, item):
	global listener_started;
	if str(item) == "Quit":
		if listener_started == True:
			server.shutdown();
			listener_started = False

			print("Exiting...");
			time.sleep(2);

		icon.stop()
	elif str(item) == "START server":
		if listener_started == False:
			threading.Thread(target=start_listener, daemon=True).start();
		else:
			print("Server already started");
	elif str(item) == "STOP server":
		server.shutdown();
		listener_started = False
		
	
    
icon = pystray.Icon("RemotInit!", image, menu=pystray.Menu(
	pystray.MenuItem("Quit", on_click),
	pystray.MenuItem("START server", on_click),
	pystray.MenuItem("STOP server", on_click),
))


def start_icon():
	print("BEGIN START icon");
	icon.run();

def is_port_in_use(port: int) -> bool:
	import socket
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		return s.connect_ex(('localhost', port)) == 0;

def kill_2011():
	terminal_kill_2011 = "";
	attempts = 0;
	max_attempts = 10;

	terminal_kill_2011 = os.popen("npx kill-port 2011").read();

	while ("Process on port 2011 killed" not in terminal_kill_2011) and (attempts < max_attempts):
		print(terminal_kill_2011);
		time.sleep(1);
		attempts = attempts + 1;


def main():
	print("BEGIN main");

	global server;

	server = HTTPServer((HOST, PORT), NeuralHTTP);

	threading.Thread(target=start_listener, daemon=True).start();
	threading.Thread(target=start_icon, daemon=True).start();
	
	while True:
		time.sleep(10000);

main()