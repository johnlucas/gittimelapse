# gittimelapse - takes screenshots of git commits

import sys
import os
import getopt

try:
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
    from git import *
except ImportError as e:
    print "You need to install selenium and git. e.g. pip install selenium; pip install git."
    print e
    sys.exit()

class MyBrowser:
    def __init__(self, chrome=False):
        if chrome:
            self.browser = webdriver.Chrome()
        else:
            self.browser = webdriver.Firefox()

    def take_screenshot(self,filename,url,w=1024,h=768):
        self.browser.get(url)
        self.browser.set_window_size(w,h)
        return self.browser.save_screenshot(filename)

    def close(self):
        self.browser.close()

def usage():
    print "usage: run.py -r project_folder -u url"

def quit(head=None,browser=None):
    print "Cleaning up..."

    if head:
        print "Restoring original head (%s)" % head
        head.checkout()
    if browser:
        print "Closing browser..."
        browser.close()

    sys.exit()

def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hr:u:c", ["help", "repo=","url=","max-commits=","images-dir=","chrome"])
    except getopt.GetoptError, err:
        usage()
        quit()

    url = None
    repodir = None
    max_commits = None
    imagedir = "files"
    chrome = False

    for o, a  in opts:
        if o in ("-h", "--help"):
            usage()
            quit()
        elif o in ("-r", "--repo"):
            repodir = a
        elif o in ("-u", "--url"):
            url = a
        elif o in ("-m", "--max-commits"):
            max_commits = a
        elif o in ("--images-dir"):
            imagedir = a
        elif o in ("-c","--chrome"):
            chrome = True

    # Mandatory parameters
    if not url or not repodir:
        usage()
        quit()

    try:
        # Getting the repo
        repo = Repo(repodir)
    except NoSuchPathError:
        print "Repo dir does not exist: %s" % repodir
        quit()
    except InvalidGitRepositoryError:
        print "Invalid git repo: %s" % repodir
        quit()
    
    # Git will be used to checkout commits
    git = repo.git

    # Saving current branch for later
    try:
        current_head = repo.head.reference
    except TypeError as t:
        print "Check your current branch: %s" % t
        quit()

    # Getting the list of commits for the current branch
    if max_commits:
        commits = repo.iter_commits(max_count=max_commits)
    else:
        commits = repo.iter_commits()

    # Converting iterator to a list to reverse the chronological order
    commits = list(commits)
    commits.reverse()

    b = MyBrowser(chrome)

    # Counter for image file names
    i=1

    for commit in commits:
        git.checkout(commit)
        pngname = os.path.join(imagedir,str(i) + ".png")

        try:
            b.take_screenshot(pngname,url)
        except WebDriverException as e:
            print "Problem occurred while taking screenshot: %s" % e
            quit(current_head,b)

        i += 1

    quit(current_head,b)

if __name__ == '__main__':
    main()
