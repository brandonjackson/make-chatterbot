#!/usr/bin/env python

"""
make-chatterbot
by Brandon Jackson
"""

import aiml
import subprocess
import os
import sys

BOT_PREDICATES = {
    "name": "KanoBot",
    "birthday": "January 1st 1969",
    "location": "London",
    "master": "Judoka",
    "website":"https://github.com/brandonjackson/make-chatterbot",
    "gender": "",
    "age": "",
    "size": "",
    "religion": "",
    "party": ""
}
# Make sure espeak exists
try:
    subprocess.call(["espeak","-q","foo"]);
    ESPEAK_INSTALLED = True
except OSError:
    ESPEAK_INSTALLED = False
    print "Warning: espeak command not found, skipping voice generation"

# Create Kernel
k = aiml.Kernel()
 
# Load the AIML files on first load, and then save as "brain" for speedier startup
if os.path.isfile("standard.brn") is False:
    k.learn("std-startup.xml")
    k.respond("load aiml b")
    k.saveBrain("standard.brn")
else:
    k.loadBrain("standard.brn")
 
# Give the bot a name and lots of other properties
for key,val in BOT_PREDICATES.items():
    k.setBotPredicate(key, val)

# Start Infinite Loop
while True:
    # Prompt user for input
    input = raw_input("> ")

    # Send input to bot
    response = k.respond(input)

    # Print chatbot's response
    print response

    # Output response as speech using espeak
    if ESPEAK_INSTALLED:
        try:
            subprocess.call(["espeak", "-s", "140", "\""+response+"\""])
        except:
            print "Unexpected error:", sys.exc_info()[0]
