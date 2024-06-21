import pystray;
import PIL.Image;

import time;
import threading;

image = PIL.Image.open("icon.png");

def on_click(icon, item):
	global listener_started;
	if str(item) == "Quit":
		icon.stop();
	elif str(item) == "START server":
		pass
	elif str(item) == "STOP server":
		pass
	

icon = pystray.Icon("RemotInit!", image, menu=pystray.Menu(
	pystray.MenuItem("Quit", on_click),
	pystray.MenuItem("START server", on_click),
));


def start_icon():
	print("BEGIN START icon");
	icon.run();

#icon.run();

def main():
	print("BEGIN main");
	threading.Thread(target=start_icon, daemon=True).start();
	
	while True:
		time.sleep(10000);
	
	pass

main();