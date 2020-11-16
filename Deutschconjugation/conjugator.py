"""Things to do when the file is imported"""
if __name__ != "__main__":
    import csv

    global conjugations, infinitives, tense_conj
    # Conjugations as 2d List of all conjugations/tenses
    # Infinitives as just the infinitive forms of all verbs -> Faster indexing
    conjugations, infinitives = [], []
    import os

    tense_conj = {"ich": 1, "du": 2, "er": 3, "ihr": 3, "wir": 4, "ihr": 5, "sie": 6}

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


def findIndex(verb: str):
    assert len(verb) > 0
    return infinitives.index(verb)


def line(row: int):
    assert row != -1
    return conjugations[row]


def findLine(verb: str):
    return line(findIndex(verb))


def format(word: str):
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


def present(verb: str, pronoun: str):
    temp = findLine(verb)
    return temp[tense_conj[pronoun]]


def simplepast(verb: str, pronoun: str):
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 6]


def presentperfect(verb: str, pronoun: str):
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 12]


def pastperfect(verb: str, pronoun: str):
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 18]


def future(verb: str, pronoun: str):
    temp = findLine(verb)
    return temp[tense_conj[pronoun] + 24]


def conjugate(verb: str, pronoun="alles", tense="present", get_all=False):
    # assert "*" not in verb

    verb = format(verb)

    tensemethods = {
        "present": present,
        "simple-past": simplepast,
        "present-perfect": presentperfect,
        "past-perfect": pastperfect,
        "future": future,
    }

    answer = str(tensemethods[tense](verb, pronoun)).strip()
    # print(answer)

    if get_all == True and len(answer) < 15:
        answer = answer + "_" * (15 - len(answer))
    return answer
