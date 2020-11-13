# Console Conjugator


## About
Hallo und guten Tag!

Have you ever had trouble conjguating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs.

As of now, the following tenses are supported:
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
### Pypi package is being remade, manually install like so:

```bash
wget https://raw.githubusercontent.com/Konjugators/console-conjugator/main/install
chmod +x
./install
```

## Usage
After installation, you can use the cli interface in Linux:
```bash
$ konjugier machen er present
er macht
```
or Windows:
```cmd
> konjugier tun er present-perfect
er tut
```

You can also use the conjugation module in scripts:
```python
from Deutschconjugation import conjugator

# Follows format verb-pronoun-tense
conjugator.conjugate("spielen", "er", "present-perfect")
>>> hat gespielt
```

This formats a\*, o\*, u\*, and s\* as ä, ö, ü, ß. This is may be useful for those lacking a German keyboard layout.
```python

from Deutschconjugation import conjugator

conjugator.format("heis*en")
>>> heißen
```
