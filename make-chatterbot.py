#!/usr/bin/env python

"""
make-chatterbot
by Brandon Jackson
"""

import aiml
import subprocess
import os
import sys

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
 
# Give the bot a name
k.setBotPredicate("name", "KanoBot")

# Start Infinite Loop
while True:
    # Prompt user for input
    input = raw_input("> ")

    # Send input to bot
    response = k.respond(input)

    # Print chatbot's response
    print response

    # Output response as speech using espeak
    # print commands.getoutput("/usr/bin/espeak -v en+f4 -p 99 -s 160 \"" + response + "\"")
    if ESPEAK_INSTALLED:
        try:
            subprocess.call(["espeak","\""+response+"\""])
        except:
            print "Unexpected error:", sys.exc_info()[0]
