import pystray
import PIL.Image

image = PIL.Image.open("icon.png")

icon = pystray.Icon("RemotInit!", image, menu=pystray.Menu(
	pystray.MenuItem("Quit", on_click),
	pystray.MenuItem("START server", on_click),
))

