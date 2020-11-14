my_file = open("Ubersetzen/german.txt", "r", encoding="utf-8")
content = my_file.read()
content = content[0:1000].split("\n")

import csvinterface
from googletrans import Translator
transmaschine = Translator()
for val in content:
    try:
        val2 = transmaschine.translate(val, dest="en")
        csvinterface.appverbs([[val, val2.text]])
    except:
        pass