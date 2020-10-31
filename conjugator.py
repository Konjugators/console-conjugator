import csv

'''Things to do when the file is imported'''
if __name__ != "__main__":
    global tohave
    tohave = ["habe", 'hast', 'hat', 'haben', 'habt', 'breaker',
            'hatte', 'hattest', 'hatte', 'hatten', 'hattet', 
            'breaker', 'gehabt']

    global conjugations, infinitives, indexDict
    #Conjugations as 2d List of all conjugations/tenses
    #Infinitives as just the infinitive forms of all verbs -> Faster indexing
    conjugations, infinitives = [], []
    #Dictionary of indexes to tenses/conjugations
    with open('verbs.csv', 'r', newline="") as file:
        verblist = csv.reader(file)
        for row in verblist:
            conjugations.append(row)
            infinitives.append(row[0])

def findIndex(verb:str):
    assert len(verb) > 0
    return infinitives.index(verb)

def line(row:int):
    assert row != -1
    return conjugations[row]

def deZuEn(word:str):
    z = 0
    val = 0
    newwrt = ""
    conv = {"a":"ä", "o":"ö", "u":"ü", "s":"ß"}
    convlist = ["a", "o", "u", "s"]
    while (val <= len(word)-1):
        if word[val] in convlist and word[val+1] == "*":
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
                return conjugations[verbnum][0][:-1]+"t"
    if pronoun.lower() == "ich":
        return conjugations[verbnum][1]
    if pronoun.lower() == "du":
        return conjugations[verbnum][2]
    if pronoun.lower() == "sie":
        return conjugations[verbnum][3] + " for \"she\" and " + conjugations[verbnum][0] + " for plural and formal You"
    if pronoun.lower() == "er" or pronoun.lower() == "es":
        return conjugations[verbnum][3]
    verblist = conjugations[verbnum]


def presentConjugate(verb:str, pronoun = "sie", tense="present"):
    assert "*" not in verb
    if tense == "present":
        return presentconjugate(verb, pronoun)
