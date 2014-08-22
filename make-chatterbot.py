#!/usr/bin/env python

"""
make-chatterbot
by Brandon Jackson
"""

import aiml
import subprocess
import os
import argparse
from MyKernel import MyKernel

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
TTS_ENABLED = True
TTS_ENGINE = "espeak"
TTS_SPEED = 140
TTS_PITCH = 50
TTS_VOICE_DEFAULT = "en"
TTS_VOICE = "en" # default only passed if using espeak
SHOW_MATCHES = False
DEVNULL = open(os.devnull, 'wb')

# Parse arguments
parser = argparse.ArgumentParser(description='a simple chatterbot interface')
parser.add_argument("-m", "--show-matches", help="show matching patterns that generated the response",
                    action="store_true", dest='matches')
parser.add_argument("-v", "--voice", help="name of voice (default=%s)" % TTS_VOICE)
parser.add_argument("-p", "--pitch", help="voice pitch (1-100, default=%d)" % TTS_PITCH)
parser.add_argument("-s", "--speed", help="voice speed in words per minute (default=%d)" % TTS_SPEED)
parser.add_argument("-e", "--engine", help="text-to-speech program (default=espeak)")
parser.add_argument("-q", "--quiet", help="no audio output produced",
                    action="store_true")
args = parser.parse_args()
if args.matches:
    SHOW_MATCHES = True
if args.quiet:
    TTS_ENABLED = False
if args.pitch:
    TTS_PITCH = args.pitch
if args.speed:
    TTS_SPEED = args.speed
if args.voice:
    TTS_VOICE = args.voice
if args.engine:
    TTS_ENGINE = args.engine

# Make sure espeak exists
if TTS_ENGINE == "espeak":
    try:
        subprocess.call(["espeak","-q","foo"])
    except OSError:
        TTS_ENABLED = False
        print "Warning: espeak command not found, skipping voice generation"
else:
    # non-espeak TTS engine being used
    pass

# Create Kernel (using our custom version of the aiml kernel class)
k = MyKernel()
 
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
    matchedPattern = k.matchedPattern(input) # note: this has to come before the 
                                             # call to respond as to reflect
                                             # the correct history
    response = k.respond(input)
    if SHOW_MATCHES:
        print "Matched Pattern: "
        print k.formatMatchedPattern(matchedPattern[0])
        print "Response: "
    print response

    # Output response as speech using espeak
    if TTS_ENABLED is False:
        pass
    elif TTS_ENGINE == "espeak":
        subprocess.call(["espeak", "-s", str(TTS_SPEED), "-v", TTS_VOICE,
                             "-p", str(TTS_PITCH), "\""+response+"\""],
                        stderr=DEVNULL)

    # Output response as speech using say
    elif TTS_ENGINE == "say":
        args = ["say","-r", str(TTS_SPEED)]
        if TTS_VOICE_DEFAULT!=TTS_VOICE:
            args.append("-v")
            args.append(TTS_VOICE)
        args.append("\""+response+"\"")
        subprocess.call(args)

    # Output response as speech using unsupported TTS engine
    else:
        subprocess.call([TTS_ENGINE, "\""+response+"\""])
