make-chatterbot
===============

By Brandon Jackson

Project started August 2014

make-chatterbot is a simple chatterbot interface that makes it easy to combine the AIML interpreter `pyAIML` with the text-to-speech program `espeak`. At the core of the AI is the open-source, prize-winning A.L.I.C.E. chatterbot. This project began as part of a project to build experiments for the [Kano](http://kano.me) computer.

Installation
------------

- Make sure you have these dependencies installed:
    - the `espeak` package
    - the `pyAIML` Python package
- Make sure `make-chatterbot.py` is executable
- From the terminal call `./make-chatterbot.py`
- When presented with a prompt, start the conversation!

Usage
-----

```
usage: make-chatterbot.py [-h] [-v VOICE] [-p PITCH] [-s SPEED] [-q]

a simple chatterbot interface

optional arguments:
  -h, --help            show this help message and exit
  -v VOICE, --voice VOICE
                        name of voice (default=en)
  -p PITCH, --pitch PITCH
                        voice pitch (1-100, default=50)
  -s SPEED, --speed SPEED
                        voice speed in words per minute (default=140)
  -q, --quiet           no audio output produced
```

To-Do List
----------

- Add header with cool ASCII image when first loaded
- Make it easy to add custom AIML files
- Add support for different TTS engines

Links
-----

- [pyAIML Homepage](http://pyaiml.sourceforge.net/)
- [eSpeak Homepage](http://espeak.sourceforge.net/)
- [A.L.I.C.E. Homepage](http://alice.pandorabots.com/)
- [Chatterbot Wikipedia Page](http://en.wikipedia.org/wiki/Chatterbot)
- [AIML Wikipedia Page](http://en.wikipedia.org/wiki/AIML)
- [Tutorial that inspired the espeak integration](http://www.iniy.org/?p=68)

Credits
-------

The AIML files in the `standard/` directory are the [A.L.I.C.E. intelligence](http://alice.pandorabots.com/) developed by Richard Wallace, and released under the GNU-GPL license. The files were taken from the "Standard AIML Files" posted [here on SourceForge](http://sourceforge.net/projects/pyaiml/files/Other%20Files/Standard%20AIML%20set/standard-aiml.zip/download) as part of the `pyAIML` package.