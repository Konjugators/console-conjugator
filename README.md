# Console Conjugator

[![PyPi version](https://pypip.in/v/console-conjugator/badge.png)](https://crate.io/packages/$REPO/)
[![Downloads](https://static.pepy.tech/personalized-badge/console-conjugator?period=total&units=international_system&left_color=brightgreen&right_color=yellow&left_text=PyPi%20Downloads)](https://pepy.tech/project/console-conjugator)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
## About
Hallo!

Have you ever had trouble conjugating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs.

The following tenses are supported (im Deutsch):
- present
- simple-past
- present-perfect
- past-perfect
- future
- conditional (future II)

To install and use this project, see this quick terminal video:
[![asciicast](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g.svg)](https://asciinema.org/a/Utrqg35SNAcpJcVunii67ZN2g)

# Install with pip
On Linux:


```bash
$ pip3 install -U console-conjugator
```

or Windows:

```cmd
> pip install -U console-conjugator
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
See our Conjugation app (coming to Google Play Store) or our Java GUI application for different conjugating methods!