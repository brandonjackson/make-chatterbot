make-chatbot
============

By Brandon Jackson

Project started August 2014

make-chatbot is a simple chatbot interface that makes it easy to combine the AIML interpreter `pyAIML` with the text-to-speech program `espeak`. This project began as part of a project to build experiments for the [Kano](http://kano.me) computer.

Usage
-----

- Make sure you have these dependencies installed:
	- the `espeak` package
	- the `pyAIML` Python package
- Make sure `make-chatbot.py` is executable
- From the terminal call `./make-chatbot.py`
- When presented with a prompt, start the conversation!

To-Do List
----------

- Add header with cool ASCII image when first loaded
- Make it easy to add custom AIML files
- Allow flags to be passed to espeak
- Add support for different TTS engines

Links
-----

- [pyAIML Homepage](http://pyaiml.sourceforge.net/)
- [eSpeak Homepage](http://espeak.sourceforge.net/)
- [AIML Wikipedia Page](http://en.wikipedia.org/wiki/AIML)

Credits
-------

The AIML files in the `standard/` directory are from the "Standard AIML Files" posted [here on SourceForge](http://sourceforge.net/projects/pyaiml/files/Other%20Files/Standard%20AIML%20set/standard-aiml.zip/download)as part of the `pyAIML` package by its creator, Cort Stratton.