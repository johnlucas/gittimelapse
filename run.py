import sys
import os

def usage():
	print "usage: run.py project_folder url"

if len(sys.argv) < 3:
	usage()
	sys.exit(1)

rootdir = sys.argv[1]
url = sys.argv[2]

# read git log
os.chdir(rootdir)
print os.getcwd()
os.system('git log')

# foreach commit 
	# checkout
	# take screenshot

# end
