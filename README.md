Git time lapse
==============
gittimelapse.py checks out git commits and takes a screenshot of the browser given a URL.
I developed the script for myself because I thought it could be interesting to see the evolution of a web page in time.
The ultimate idea is to create a video out of all the screenshots gittimelapse.py generates. I've created this one using iPhoto but I'd like to implement a programmatic way using opencv library probably.


Install Requirements
--------------------
gittimelapse.py requires selenium and pythongit. You can install them using pip:

    pip install selenium
    pip install gitpython

How to use it
-------------
gittimelapse.py takes two mandatory arguments:
- the path to the git repo
- the url of the web page within the git project

Just make sure you run the webserver for your git repo and then run:

    gittimelapse.py [options] project_folder url
    
For example:

    python gittimelapse.py /Users/johnlucas/Dropbox/Coding/mvpeers/ http://localhost:3000
