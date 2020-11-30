"""
This application conjugates the verbs of multiple languages
Copyright (C) 2020 Konjugators
See LICENSE for more information
"""
import csv
import os
import platform
# Load CSV when file is imported:
if __name__ != "__main__":
    import csv
    import os

    # ASCII colors:
    colors = {
        "Black": "\u001b[30m",
        "Red": "\u001b[31m",
        "Green": "\u001b[32m",
        "Yellow": "\u001b[33m",
        "Blue": "\u001b[34m",
        "Magenta": "\u001b[35m",
        "Cyan": "\u001b[36m",
        "White": "\u001b[37m",
        "Reset": "\u001b[0m",
    }

    global conjugations, infinitives, tense_conj
    # Conjugations as 2d List of all conjugations/tenses
    # Infinitives as just the infinitive forms of all verbs -> Faster indexing
    conjugations, infinitives = [], []

    tense_conj = {"ich": 1, "du": 2, "er": 3, "wir": 4, "ihr": 5, "sie": 6}

    this_dir, this_filename = os.path.split(__file__)
    path = os.path.join(this_dir, "verbs.csv")
    with open(path, "r", newline="", encoding="utf-8") as file:
        verblist = csv.reader(file)
        for row in verblist:
            try:
                conjugations.append(row)
                infinitives.append(row[0])
            except:
                conjugations.append([])
                infinitives.append("")

# CSV indexing and searching methods
def findIndex(verb: str) -> str:
    assert len(verb) > 0
    return infinitives.index(verb)


def line(row: int) -> str:
    assert row != -1
    return conjugations[row]


def findLine(verb: str) -> str:
    return line(findIndex(verb))


# Formatting for those without german keyboard
def format(word: str) -> str:
    if "^" not in word:
        return word
    z = 0
    val = 0
    newwrt = ""
    conv = {"a": "ä", "o": "ö", "u": "ü", "s": "ß"}
    convlist = ["a", "o", "u", "s"]
    while val <= len(word) - 1:
        if word[val] in convlist and word[val + 1] == "^":
            newwrt += conv[word[val]]
            val += 2
        else:
            newwrt += word[val]
            val += 1
    return newwrt


def colorize(text: str, tense) -> str:
    textlist = text.split(" ")
    texts = text
    if len(textlist) == 2:
        texts = (
            colors["Green"]
            + textlist[0].strip()
            + colors["Magenta"]
            + " "
            + textlist[1].strip()
            + colors["Reset"]
        )
    if len(textlist) == 3 and (tense == "present" or tense == "simple-past"):
        texts = (
            colors["Green"]
            + textlist[0].strip()
            + colors["Magenta"]
            + " "
            + textlist[1].strip()
            + colors["Blue"]
            + " "
            + textlist[2].strip()
            + colors["Reset"]
        )
    elif len(textlist) == 3:
        texts = (
            colors["Green"]
            + textlist[0].strip()
            + colors["Red"]
            + " "
            + textlist[1].strip()
            + colors["Magenta"]
            + " "
            + textlist[2].strip()
            + colors["Reset"]
        )
    return texts


# All tenses conjugation:
def present(verb: str, pronoun: str) -> str:
    temp = findLine(verb)
    return temp[tense_conj[pronoun]]


def simplepast(verb: str, pronoun: str) -> str:
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 6]


def presentperfect(verb: str, pronoun: str) -> str:
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 12]


def pastperfect(verb: str, pronoun: str) -> str:
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 18]


def future(verb: str, pronoun: str) -> str:
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 24]


# Header conjugate: Branches to different methods
def conjugate(verb: str, pronoun="alles", tense="present", color=False) -> str:
    verb = format(verb)

    tensemethods = {
        "present": present,
        "simple-past": simplepast,
        "present-perfect": presentperfect,
        "past-perfect": pastperfect,
        "future": future,
    }
    answer = str(tensemethods[tense](verb, pronoun)).strip()
    if color:
        answer = colorize(answer, tense)
    return answer


def allPronounsConjugate(verb, tense, ANSI = False) -> str:
    conj = conjugate
    temp = []
    temp2 = []
    for val in ["ich", "du", "er", "wir", "ihr", "sie"]:
        if ANSI:
            temp.append(conj(verb, val, tense, True))
        else:
            temp.append(conj(verb, val, tense, False))
        temp2.append(conj(verb, val, tense, False))

    greatest = 0
    for val in temp2:
        if len(val) > greatest:
            greatest = len(val)

    

    for z in range(len(temp)):
        if len(temp2[z]) < greatest:
            temp[z] = temp[z] + " " * (greatest - len(temp2[z]))
            # print(temp[z])

    minus = (
        lambda symbol: f"{symbol}" * greatest * 2
        + f"{symbol}" * 4
        + f"{symbol}" * 3
        + f"{symbol}" * len("1st Person: ")
    )
    temp_str = (
        minus("_")
        + f"\n\
|          |singular{' '*(greatest-len('singular'))}   |plural{' '*(greatest-len('plural'))}  |\n{minus('—')}\n\
|1st Person| {temp[0]}  |{temp[3]}  |\n{minus('—')}\n\
|2nd Person| {temp[1]}  |{temp[4]}  |\n{minus('—')}\n\
|3rd Person| {temp[2]}  |{temp[5]}  |\n"
        + minus("‾")
    )
    return temp_str


def allConjugate(verb, tenses, colors = False) -> str:
    fullText = ""

    if tenses[0].lower() == "alles" or tenses[0].lower() == "a":
        tenses = ["present", "simple-past", "present-perfect", "past-perfect", "future"]

    for tense in tenses:
        fullText += f"The {tense} tense:\n" + allPronounsConjugate(verb, tense, colors) + "\n"
    print(fullText)
