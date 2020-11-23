#!/usr/bin/env python3
import argparse
import sys

# Parse Args
def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', nargs= 1)
    parser.add_argument("i", nargs=("?" if 'f' in sys.argv else 3), help="The unconjugated verb")

    args = parser.parse_args()
    return args


# Change words in german to english, so that the conjugation process works properly
def tensePreprocessing(tense: str) -> str:
    if tense in ["präsens"]:
        return "present"
    if tense in ["simplepast", "präteritum", "prateritum"]:
        return "simple-past"
    if tense in ["presentperfect", "perfekt"]:
        return "present-perfect"
    if tense in ["plusquamperfect", "pastperfect", "pastPerfect"]:
        return "past-perfect"
    if tense in ["zukunft"]:
        return "future"
    else:
        return tense

# Literally translates to "Mode understanding - c and f are the mode arguments"
def modeVerstehen():
    args = get_args()
    if args.mode[0] == "f":
        from Deutschconjugation import fuzzy
        fuzzy.start()
    if args.mode[0] == "c":
        from Deutschconjugation import conjugator as conj
        infinitive, pronoun, tense = lower_format()
        tense = tensePreprocessing(tense)
        z = conj.conjugate(infinitive, pronoun, tense)
        print(z)

# Lower_case the args
def lower_format():
    args = get_args()
    if len(args.i) < 3:
        raise("You are missing a few things")
        print("error")
    if len(args.i) > 3:
        raise("You have too many things")
    return args.i[0].lower(), args.i[1].lower(), args.i[2].lower()
    # infinitive.lower(), args.pronoun, args.tense.lower()

# Conjugate and print args
def main():
    modeVerstehen()

if __name__ != "__main__":
    import argparse

# TODO Table
