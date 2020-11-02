"""Things to do when the file is imported"""
if __name__ != "__main__":
    import csv

    global tohave
    tohave = [
        "habe",
        "hast",
        "hat",
        "haben",
        "habt",
        "breaker",
        "hatte",
        "hattest",
        "hatte",
        "hatten",
        "hattet",
        "breaker",
        "gehabt",
    ]
    tobe = [
        "bin",
        "bist",
        "ist",
        "sind",
        "seid",
        "breaker",
        "war",
        "warst",
        "war",
        "waren",
        "wart",
        "breaker",
        "gewesen",
    ]

    global conjugations, infinitives, indexDict
    # Conjugations as 2d List of all conjugations/tenses
    # Infinitives as just the infinitive forms of all verbs -> Faster indexing
    conjugations, infinitives = [], []
    # Dictionary of indexes to tenses/conjugations
    import os

    this_dir, this_filename = os.path.split(__file__)
    path = os.path.join(this_dir, "verbs.csv")
    with open(path, "r", newline="") as file:
        verblist = csv.reader(file)
        for row in verblist:
            conjugations.append(row)
            infinitives.append(row[0])


def findIndex(verb: str):
    assert len(verb) > 0
    return infinitives.index(verb)


def line(row: int):
    assert row != -1
    return conjugations[row]


def format(word: str):
    z = 0
    val = 0
    newwrt = ""
    conv = {"a": "ä", "o": "ö", "u": "ü", "s": "ß"}
    convlist = ["a", "o", "u", "s"]
    while val <= len(word) - 1:
        if word[val] in convlist and word[val + 1] == "*":
            newwrt += conv[word[val]]
            val += 2
        else:
            newwrt += word[val]
            val += 1
    return newwrt


def presentconjugate(verb, pronoun):
    verbnum = infinitives.index(verb)
    if pronoun.lower() == "ihr":
        if conjugations[verbnum][0][-1] == "n":
            if conjugations[verbnum][0][-2] == "e":
                return conjugations[verbnum][0][:-2] + "t"
            else:
                return conjugations[verbnum][0][:-1] + "t"
    if pronoun.lower() == "ich":
        return conjugations[verbnum][1]
    if pronoun.lower() == "du":
        return conjugations[verbnum][2]
    if pronoun.lower() == "sie":
        return (
            conjugations[verbnum][0]
            )
    if pronoun.lower() == "er" or pronoun.lower() == "es":
        return conjugations[verbnum][3]
    if pronoun.lower() == "wir":
        return conjugations[verbnum][0]
    verblist = conjugations[verbnum]


def conjugate(verb: str, pronoun="alles", tense="present"):
    assert "*" not in verb
    if tense == "present":
        answer= presentconjugate(verb, pronoun)
    if tense == "present-perfect":
        answer = presentperfectconjugate(verb, pronoun)
    if tense == "imperative":
        answer =imperativeconjugate(verb, pronoun)
    if tense == "partizip-1":
        answer= partizip1conjugate(verb)
    answer = str(answer)
    
    if len(answer) < 10:
        answer = answer + " "*(10-len(answer))
    return answer

def presentperfectconjugate(verb: str, pronoun: str):
    verbnum = infinitives.index(verb)
    if conjugations[verbnum][9] == "haben":
        hilfensverb = tohave
    elif conjugations[verbnum][9] == "sein":
        hilfensverb = tobe
    else:
        return 1
    if pronoun == "er" or pronoun == "es":
        hilfensverb = hilfensverb[2]
    if pronoun.lower() == "sie":
        hilfensverb = hilfensverb[3]
    if pronoun == "ich":
        hilfensverb = hilfensverb[0]
    if pronoun == "du":
        hilfensverb = hilfensverb[1]
    if pronoun == "ihr":
        hilfensverb = hilfensverb[4]
    if pronoun == "wir":
        hilfensverb = hilfensverb[3]
    return str(hilfensverb) + " " + str(conjugations[verbnum][5])


def imperativeconjugate(verb: str, pronoun: str):
    verbnum = infinitives.index(verb)
    if pronoun == "du":
        conj = conjugations[verbnum][7]
        
    elif pronoun == "ihr":
        conj = conjugations[verbnum][8]
    elif pronoun == "sie" or pronoun == "wir":
        conj = conjugations[verbnum][7] + "en"
    else:
        conj = "Nonee"

    if conj[-1] == "e":
        return conj[:-1]
    else:
        return conj


def partizip1conjugate(verb: str):
    verbnum = infinitives.index(verb)
    return conjugations[verbnum][0] + "d"
