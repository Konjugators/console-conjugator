# Console Conjugator

[![PyPi version](https://pypip.in/v/console-conjugator/badge.png)](https://pypi.org/project/console-conjugator/)
[![Downloads](https://static.pepy.tech/personalized-badge/console-conjugator?period=total&units=international_system&left_color=brightgreen&right_color=yellow&left_text=PyPi%20Downloads)](https://pepy.tech/project/console-conjugator)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## About
Hallo!

Have you ever had trouble conjugating verbs in different languages? Forgot the simple-past of "machen"
in german, or perhaps the various conjugations of "dire"?

Fear not! Console-conjugator easily allows you to conjugate thousands of verbs from the command-line!

# Installation

## Install with pip
```bash
pip/pip3 install console-conjugator
```
## Install Script
```bash
git clone https://github.com/Konjugators/console-conjugator.git && cd console-conjugator/bin
chmod +x install
./install
```

#### Installation Video and Demo

[![asciicast](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g.svg)](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g)


# Usage
### After installation, you can use the cli interface in most terminals and scripts

###### --NOTE--
This Documentation will be moved to readthedocs soon. 

The following tenses are supported (im Deutsch):
- present
- simple-past
- present-perfect
- past-perfect
- future
- future2

Just give the argument "c" (for "command line") and conjugate away:
```bash
$ konjugier c machen er present
er macht
```
You can also create a table of conjugations:
```bash
konjugier a machen a
```
Replace "a" with a specific tense, if wanted: a will result in tables for all tenses.
To use the fuzzy finder, simply give the argument "f" (Not fully supported):
```bash
$ konjugier f
```
Note: Fuzzy Finder is only availible on OS X and Linux distributions

The character-set a^, o^, u^, and s^ will be formatted automatically to ä, ö, ü, and ß (for german) most of the time (full support added soon).

## RoadMap:
- [ ] Fuzzy Finder Revamp: Select pronoun and tense in fzf format
- [ ] French - finish
- [ ] Spanish Conjugation
