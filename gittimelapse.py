# gittimelapse - takes screenshots of git commits

import sys
import os
import getopt

try:
    from selenium import webdriver
    from selenium.common.exceptions import WebDriverException
    from git import *
except ImportError as e:
    print "You need to install selenium and git. e.g. pip install selenium; pip install gitpython."
    print e
    sys.exit(2)

def clean_up(head=None,webdriver=None):
    print "Cleaning up..."

    if head:
        print "Restoring original head (%s)" % head
        head.checkout()
        
    if webdriver:
        print "Closing browser"
        webdriver.close()

def get_repo(repodir):
    try:
        return Repo(repodir)
    except NoSuchPathError:
        print "Repo dir does not exist."
        raise
    except InvalidGitRepositoryError:
        print "Invalid git repo."
        raise

def get_head(repo):
    # Saving current branch for later
    try:
        return repo.head.reference
    except TypeError:
        print "Check your current branch."
        raise
        
def get_commits(repo,max_commits):
    try:
        # Getting the list of commits for the current branch
        if max_commits:
            commits = repo.iter_commits(max_count=max_commits)
        else:
            commits = repo.iter_commits()

        # Converting iterator to a list to reverse the chronological order
        commits = list(commits)
        commits.reverse()
        
        return commits
    except Exception, e:
        print "Error getting commits."
        raise

def get_webdriver(chrome):
    if not chrome:
        return webdriver.Firefox()
    else:
        return webdriver.Chrome()
        
def take_screenshot(webdriver,filename,url,w=1024,h=768):
    webdriver.get(url)
    webdriver.set_window_size(w,h)
    return webdriver.save_screenshot(filename)
                
def take_screenshots(webdriver,repo,commits,imagedir,url,chrome):
    # Git command will be used to checkout commits
    git = repo.git
    i=1 # Counter for image file names
    
    for commit in commits:
        git.checkout(commit)
        pngname = os.path.join(imagedir,str(i) + ".png")
    
        try:
            if not take_screenshot(webdriver,pngname,url):
                raise Exception("Could not save image %s" %pngname)
        except Exception, e:
            print "Problem occurred while taking screenshot."
            raise
    
        i += 1

    

def usage():
    print """usage: gittimelapse.py [options] project_folder url
Options:
    -h, --help
        Show this help.
    --max-commits=<number>
        Limits the number of commits starting from the most recent.
    --images-dir=<path> # this doesn't work yet
        Default is the relative path "./files"
    -c, --chrome 
        Default webdriver is Firefox. Chrome needs its executable in the PATH.
        It can be downloaded here: http://code.google.com/p/chromedriver/downloads/list
"""
           
def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc", [
            "help", "max-commits=","images-dir=","chrome"])
    except getopt.GetoptError, err:
        usage()
        sys.exit(2)

    # Default vars
    url = None
    repodir = None
    max_commits = None
    imagedir = "files"
    chrome = False

    for o, a  in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-m", "--max-commits"):
            max_commits = a
        elif o in ("--images-dir"):
            imagedir = a
        elif o in ("-c","--chrome"):
            chrome = True

    if len(args) < 2:
        usage()
        sys.exit(2)

    repodir = args[0]
    url = args[1]
    head = None
    webdriver = None
    
    try:
        print "Getting Repo"
        repo = get_repo(repodir)
        print "Getting Head"
        head = get_head(repo)
        print "Getting Commits"
        commits = get_commits(repo,max_commits)
        webdriver = get_webdriver(chrome)
        print "Taking Screenshots"
        take_screenshots(webdriver,repo,commits,imagedir,url,chrome)
    except Exception, e:
        print e
        sys.exit()
    finally:
        clean_up(head,webdriver)
    
if __name__ == '__main__':
    main()