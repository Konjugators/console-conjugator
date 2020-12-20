import os
import csv


if __name__ != "__main__" or __name__ == "__main__":
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

    global conjugations, infinitives, pronouns
    # Conjugations as 2d List of all conjugations/tenses
    # Infinitives as just the infinitive forms of all verbs -> Faster indexing
    conjugations, infinitives = [], []

    pronouns = {
        "je": 0,
        "tu": 1,
        "on": 2,
        "nous": 3,
        "vous": 4,
        "ils": 5,
    }

    tenses = {
    "present": 3,
    "imperfect": 9,
    "simple-past": 15,
    "future": 21,
    "conditional": 27
    }

    this_dir, this_filename = os.path.split(__file__)
    path = os.path.join(this_dir, "frenchverbs.csv")
    with open(path, "r", newline="", encoding="utf-8") as file:
        verblist = csv.reader(file)
        for row in verblist:
            conjugations.append(row)
            infinitives.append(row[0])

def findIndex(verb: str) -> str:
    assert len(verb) > 0
    return infinitives.index(verb)

def conjugate(infinitive:str, pronoun:str, tense:str, color:bool=False)->str:
    # ["present", "past", "simple-past", "future", "imperfect", "conditional"]
    row = conjugations[findIndex(infinitive)]
    z = f""
    idx = 0
    if tense == "past":
        if "avoir" in row:
            helper = "avoir"
        else:
            helper = "être"
        z = f"{pronoun} {conjugate(helper, pronoun, 'present')} {row[1]}"
    else:
        idx += tenses[tense]
        idx += pronouns[pronoun]
        z = f"{pronoun} {row[idx]}"
    return z


# DONT DELETE
"""
['infinitive',
 'past participle',
 'helper',
 'indicative|present|first person singular',
 'indicative|present|second person singular',
 'indicative|present|third person singular',
 'indicative|present|first person plural',
 'indicative|present|second person plural',
 'indicative|present|third person plural',
 'indicative|imperfect|first person singular',
 'indicative|imperfect|second person singular',
 'indicative|imperfect|third person singular',
 'indicative|imperfect|first person plural',
 'indicative|imperfect|second person plural',
 'indicative|imperfect|third person plural',
 'indicative|past historic|first person singular',
 'indicative|past historic|second person singular',
 'indicative|past historic|third person singular',
 'indicative|past historic|first person plural',
 'indicative|past historic|second person plural',
 'indicative|past historic|third person plural',
 'indicative|future|first person singular',
 'indicative|future|second person singular',
 'indicative|future|third person singular',
 'indicative|future|first person plural',
 'indicative|future|second person plural',
 'indicative|future|third person plural',
 'indicative|conditional|first person singular',
 'indicative|conditional|second person singular',
 'indicative|conditional|third person singular',
 'indicative|conditional|first person plural',
 'indicative|conditional|second person plural',
 'indicative|conditional|third person plural',
 ------------------------------------------------
 'subjunctive|present|first person singular',
 'subjunctive|present|second person singular',
 'subjunctive|present|third person singular',
 'subjunctive|present|first person plural',
 'subjunctive|present|second person plural',
 'subjunctive|present|third person plural',
 'subjunctive|imperfect|first person singular',
 'subjunctive|imperfect|second person singular',
 'subjunctive|imperfect|third person singular',
 'subjunctive|imperfect|first person plural',
 'subjunctive|imperfect|second person plural',
 'subjunctive|imperfect|third person plural']
"""