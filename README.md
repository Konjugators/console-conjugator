# Console Conjugator

[![PyPi version](https://pypip.in/v/console-conjugator/badge.png)](https://pypi.org/project/console-conjugator/)
[![Downloads](https://static.pepy.tech/personalized-badge/console-conjugator?period=total&units=international_system&left_color=brightgreen&right_color=yellow&left_text=PyPi%20Downloads)](https://pepy.tech/project/console-conjugator)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## About
Hallo!

Have you ever had trouble conjugating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs. See Usage for more information on how to use this tool. 


# Installation

## Install with pip
On Linux:

```bash
$ pip3 install console-conjugator
```

or Windows:
```cmd
> pip install console-conjugator
```

## Install with install script
```bash
git clone https://github.com/Konjugators/console-conjugator.git && cd console-conjugator
sudo chmod +x install
./install
```

Installation Video and Demo:
[![asciicast](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g.svg)](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g)


# Usage
### After installation, you can use the cli interface in most terminals and scripts

The following tenses are supported (im Deutsch):
- present
- simple-past
- present-perfect
- past-perfect
- future
Coming Soon:
- conditional (future II)

Just give the argument "c" (for "command line") and conjugate away:
```bash
$ konjugier c machen er present
er macht
```
You can also create a table of conjugations:
```bash
konjugier a machen alles
```
Replace "alles" with a specific tense, if wanted: alles will result in tables for all tenses.
To use the fuzzy finder, simply give the argument "f" (Not fully supported):
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
The character-set a^, o^, u^, and s^ will be formatted automatically to ä, ö, ü, and ß (for german) most of the time (full support added soon).

# Progress

## Development Progress
French conjugation is underway, and will be added soon.

## Finished:
### - Deutsch -
- [X] Create Deutsch Conjugation module
- - [ ] Add Futur II support
- [X] Create CLI interface
- [X] Connect CLI with Deutsch Conjugation
- [X] Fuzzy Finder for Deutsch
- [X] Add optional arguments to access both conjugation and fuzzy finder from CLI
- - [X] Revamp Optional Arguments with Conditional Arguments
- [ ] Latest version PyPi Upload

## Work in Progress:
### - Français - 
- [ ] Create French Conjugation module
- [ ] Create CLI for Spanish
- [ ] Connect CLI with French Conjugation
- [X] Fuzzy Finder for French (same across modules)
- [ ] PyPi Upload

### - Española - 
- [ ] Create Spanish Conjugation module
- [ ] Create CLI for Spanish
- [ ] Connect CLI with Spanish Conjugation
- [X] Fuzzy Finder for Spanish (same across modules)
- [ ] PyPi Upload

## RoadMap (Further):
- [ ] Fuzzy Finder Revamp: Select pronoun and tense in fzf format
- [X] Create German Dictionary csv (Deutsch -> Englisch)
- - [ ] Corresponding CommandLine interface
- [ ] French Dictionary (Français -> l'anglais)
- [ ] Spanish Dictionary (Española -> ingles)


# Alternatives:
See our Conjugation app (coming to Google Play Store) or our Java Swing application for different conjugating methods!
