# Console Conjugator

## Install with pip
On Linux:
```sh
$ pip3 install console-conjugator
```
or Windows:
```cmd
> pip install console-conjugator
```

## Usage
After installation, you can use the cli interface in Linux:
```sh
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

## About
Hallo und guten Tag!

Have you ever had trouble conjguating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs.

As of now, the following tenses are supported:
1. present
2. present-perfect
3. imperative
4. partizip1
