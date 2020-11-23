# Console Conjugator


## About
Hallo!

Have you ever had trouble conjguating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs.

As of now, the following tenses are supported (in german):
1. Future (Zukunft)
2. present (Präsens)
3. present-perfect (Perfekt)
4. simple-past (Präteritum)
5. past-perfect (Plusquamperfekt)

## Install with pip
On Linux:


```bash

$ pip3 install console-conjugator

```

or Windows:

```cmd

> pip install console-conjugator

```

## Usage
After installation, you can use the cli interface in most terminals and scripts:
```bash
$ konjugier machen er present
er macht
```

You can also use the conjugation module in python scripts:
```python
from Deutschconjugation import conjugator

# Follows format verb-pronoun-tense
conjugator.conjugate("spielen", "er", "present-perfect")
>>> hat gespielt
```
The character-set a*, o*, u*, and s* will be formatted automatically to ä, ö, ü, and ß (for german).

A French Module will be soon added to this package.

Official Fuzzy Finder support to be added soon.
