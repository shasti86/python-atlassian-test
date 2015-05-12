Atlassian Chat Message Decoder
==============================
This is micro utility that accepts a chat message via CLI and parse the names, emoticons, links and titles of the website. This will return a string (a valid json as well) will all the parsed information.

SETUP
=====
1. Install python 2.7
    Install debian dependancies

BUILD
=====

Install project dependencies

sudo python setup.py install

RUN UNIT TESTS
==============

./build.sh

RUN
===
python run.py -M/--msg "chat message"

SAMPLE CONFIG
=============

LOGGING = {
    'log_level': 'INFO',
    'log_file': '/tmp/chatmsg.log'
}

ABOUT THE CODE
==============


FUTURE ENHANCEMENTS
===================
To build a nice UI (using AngularJS or JINJA2 with Bottle API) to display the real time chat reports with MongoDB as the backed data store. 

CONTACT
=======

Please send bugs, ideas and other feedback to 
shastinathan.s@gmail.com