#!/usr/bin/env python

"""
make-chatterbot
by Brandon Jackson
"""

import aiml
import subprocess
import os
import argparse

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
ESPEAK_ENABLED = True
ESPEAK_SPEED = 140
ESPEAK_PITCH = 50
ESPEAK_VOICE = "en"

# Parse arguments
parser = argparse.ArgumentParser(description='a simple chatterbot interface')
parser.add_argument("-v", "--voice", help="name of voice (default=%s)" % ESPEAK_VOICE)
parser.add_argument("-p", "--pitch", help="voice pitch (1-100, default=%d)" % ESPEAK_PITCH)
parser.add_argument("-s", "--speed", help="voice speed in words per minute (default=%d)" % ESPEAK_SPEED)
parser.add_argument("-q", "--quiet", help="no audio output produced",
                    action="store_true")
args = parser.parse_args()
if args.quiet:
    ESPEAK_ENABLED = False
if args.pitch:
    ESPEAK_PITCH = args.pitch
if args.speed:
    ESPEAK_SPEED = args.speed
if args.voice:
    ESPEAK_VOICE = args.voice

# Make sure espeak exists
try:
    subprocess.call(["espeak","-q","foo"])
except OSError:
    ESPEAK_ENABLED = False
    print "Warning: espeak command not found, skipping voice generation"

# Create Kernel
k = aiml.Kernel()
 
# Load the AIML files on first load, and then save as "brain" for speedier startup
if os.path.isfile("cache/standard.brn") is False:
    k.learn("aiml/standard/std-startup.xml")
    k.respond("load aiml b")
    k.saveBrain("cache/standard.brn")
else:
    k.loadBrain("cache/standard.brn")
 
# Give the bot a name and lots of other properties
for key,val in BOT_PREDICATES.items():
    k.setBotPredicate(key, val)

# Start Infinite Loop
while True:
    # Prompt user for input
    input = raw_input("> ")

    # Send input to bot and print chatbot's response
    response = k.respond(input)
    print response

    # Output response as speech using espeak
    if ESPEAK_ENABLED:
        subprocess.call(["espeak", "-s", str(ESPEAK_SPEED), "-v", ESPEAK_VOICE,
                             "-p", str(ESPEAK_PITCH), "\""+response+"\""])
