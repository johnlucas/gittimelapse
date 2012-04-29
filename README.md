Git time lapse
==============
gittimelapse.py checks out git commits and takes screenshots of the web browser given a URL.
I developed the script for myself because I thought it could be interesting to see the evolution of a web page in time.
The ultimate idea is to create a video out of all the screenshots gittimelapse.py generates. I've created this one using iPhoto but I'd like to implement an automatic video creation probably using the <a href="http://sourceforge.net/projects/opencvlibrary/">opencv</a> library.


Install Requirements
--------------------
gittimelapse.py requires selenium and pythongit. You can install them using pip:

    pip install selenium
    pip install gitpython

How to use it
-------------
gittimelapse.py takes two mandatory arguments: a `/path/to/repo` and the url of a web page within the given git repo

Just make sure you run the webserver for your git repo and then run:

    gittimelapse.py [options] /path/to/repo url
    
For example:

    python gittimelapse.py /Users/johnlucas/Dropbox/Coding/mvpeers/ http://localhost:3000

Selenium Webdriver
------------------
By default I am using Firefox because WebDriver doesn't need an extra binary for that. If you want to use chrome you need to download the <a href="http://code.google.com/p/chromedriver/downloads/list">driver</a> binary and put it in your PATH.