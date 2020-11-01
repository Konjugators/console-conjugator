# Console Conjugator

Hallo und guten Tag!

Have you ever had trouble conjguating your verbs? Forgot "machen" in present-perfect, or maybe "tun" for the pronoun "ihr"? 
This project may be useful to you! We can help you conjugate almost all of the german standard verbs.
To install this project, python is required.

On Linux:
```bash
pip3 install console-conjugator
```
or Windows:
```cmd
pip install console-conjugator
```

To test out your new install, open up a python REPL or file, and import the following:
```python
from Deutschconjugation import conjugator
```
Then you can use it simply as such:
```python
conjugator.format("heis*en")
[0] heißen
```
This formats a*, o*, u*, and s* as ä, ö, ü, ß. Might be useful for those lacking a german keyboard layout.
To conjugate verbs, you can simply use the conjugate interface:
```python
# Follows format verb-pronoun-tense
conjugator.conjugate("spielen", "er", "present-perfect")
[0] hat gespielt
```
As of now, the following tenses are supported for most verbs:
1. present
2. present-perfect
3. partizip1
4. imperative

If the method is not given the tense argument, it is assumed to be present.

Thank you for checking out our project, and have a good day!
-Shynn Lawrence, Govind Gnanakumar
