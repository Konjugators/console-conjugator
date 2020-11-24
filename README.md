# Console Conjugator


## About
Hallo!

Have you ever had trouble conjguating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs.

To install and use this project, see this quick terminal video:
![[asciicast](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g.svg)](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g)

# Install with pip
On Linux:


```bash

$ pip3 install console-conjugator

```

or Windows:

```cmd

> pip install console-conjugator

```

# Usage
### After installation, you can use the cli interface in most terminals and scripts

Just give the argument "c" (for "command line") and conjugate away:
```bash
$ konjugier c machen er present
er macht
```
To use the fuzzy finder, simply give the argument "f" (fuzzy finder) and be on your way:
```bash
$ konjugier f
```
Note: Fuzzy Finder is only availible on OS X and Linux distributions


You can also use the conjugation module in python scripts:
```python
>>> from Deutschconjugation import conjugator
>>> # Follows format verb-pronoun-tense
>>> conjugator.conjugate("spielen", "er", "present-perfect")
hat gespielt
```
The character-set a^, o^, u^, and s^ will be formatted automatically to ä, ö, ü, and ß (for german).

# Progress
## Finished:
### - Deutsch -
- [X] Create Deutsch Conjugation module
- [X] Create CLI interface
- [X] Connect CLI with Deutsch Conjugation
- [X] Fuzzy Finder for Deutsch
- [X] Add optional arguments to access both conjugation and fuzzy finder from CLI
- [X] PyPi Upload

## Work in Progress:
### - Français - 
- [ ] Create French Conjugation module
- [ ] Create CLI for Spanish
- [ ] Connect CLI with French Conjugation
- [ ] Fuzzy Finder for French
- [ ] PyPi Upload

### - Española - 
- [ ] Create Spanish Conjugation module
- [ ] Create CLI for Spanish
- [ ] Connect CLI with Spanish Conjugation
- [ ] Fuzzy Finder for Spanish
- [ ] PyPi Upload

## RoadMap (Further):
- [ ] German Dictionary (Deutsch -> Englisch)
- [ ] French Dictionary (Français -> l'anglais)
- [ ] Spanish Dictionary (Española -> ingles)


# Alternatives:
See our Conjugation app (coming to google play store) or our Java GUI application for different conjugating methods!
