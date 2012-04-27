import sys
import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from git import *

class MyBrowser:
	def __init__(self):
		self.browser = webdriver.Chrome()
	
	def take_screenshot(self,filename,url,w=1024,h=768):
		self.browser.get(url)
		self.browser.set_window_size(w,h)
		return self.browser.save_screenshot(filename)

	def close(self):
		self.browser.close()

def usage():
	print "usage: run.py project_folder url"

def quit():
	try:
		print "Restoring original head (%s)" % current_head
		current_head.checkout()
		b.close()
	except NameError:
		pass

	sys.exit()

if len(sys.argv) < 3:
	usage()
	sys.exit(1)

repodir = sys.argv[1]
url = sys.argv[2]
imagedir = "files"
max_count=5

repo = Repo(repodir)
git = repo.git

try:
	current_head = repo.head.reference
except TypeError as t:
	print "Check your current branch: %s" % t
	quit()

if max_count:
	commits = repo.iter_commits(max_count=5)
else:
	commits = repo.iter_commits()
	
b = MyBrowser()
i=1

for commit in commits:
	git.checkout(commit)
	pngname = imagedir + "/" + str(i) + ".png"
	try:
		b.take_screenshot(pngname,url)
	except WebDriverException:
		print "Problem occurred while taking screenshot. Check if the server on your repo is up and running."
		quit()
		
	i += 1

quit()
