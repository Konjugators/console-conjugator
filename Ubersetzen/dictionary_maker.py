my_file = open("Ubersetzen/german.txt", "r", encoding="utf-8")
content = my_file.read()
content = content.split("\n")


import csvinterface
from googletrans import Translator

transmaschine = Translator()
x = 0  # Progress update
z = lambda a: transmaschine.translate(a, dest="en", src="de")
for val in content:
    try:
        temp = z(val).text
        if temp != val:
            csvinterface.appverbs([[val, temp]])
        else:
            pass
    except:
        pass
    if x % 100 == 0:
        print("Currently at index: " + str(x))
    x += 1
