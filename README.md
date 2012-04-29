Git time lapse
==============
gittimelapse.py checks out git commits and takes screenshots of the web browser given a URL.
I developed the script for myself because I thought it could be interesting to see the evolution of a web page in time.
The ultimate idea is to create a video out of all the screenshots gittimelapse.py generates. I've created <a href="https://www.dropbox.com/s/ktuiceg2yajtmld/video.mov">this one</a> using iPhoto but I'd like to implement an automatic video creation probably using the <a href="http://sourceforge.net/projects/opencvlibrary/">opencv</a> library.


Install Requirements
--------------------
gittimelapse.py requires selenium and pythongit. You can install them using pip:

    $ pip install selenium
    $ pip install gitpython

How to use it
-------------
Make sure your run the web server. In this example a simple `rails s` will do:

    $ rails s
    
Then run gittimelapse, it will store all the images into the relative path './files'. You can override the behaviour with the option --images-dir:

    $ python gittimelapse.py -c /Users/johnlucas/Coding/mvpeers http://localhost:3000 
    Getting Repo
    Getting Head
    Getting Commits
    Taking Screenshots
    Cleaning up...
    Restoring original head (master)
    $

The script will get the list of all your commits for your current branch, will fire a browser and take a screenshot of each commit checkout. Eventually it will restore the original HEAD.

Selenium Webdriver
------------------
The default browser is Firefox because WebDriver doesn't need an extra binary for that. If you want to use chrome you need to download the <a href="http://code.google.com/p/chromedriver/downloads/list">driver</a> binary and put it in your PATH and then run gittimelapse.py with the -c or --chrome option:

    python gittimelapse.py -c /Users/johnlucas/Dropbox/Coding/mvpeers/ http://localhost:3000