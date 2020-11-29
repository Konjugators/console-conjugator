#!/usr/bin/env python3
import argparse
import sys

# Parse Args
def get_args()->str:
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', nargs= 1, help="The conjugation functions that can be performed (f->fuzzy, c->conjugate, a->alles). \
        Add the -h flag after selecting a mode to see in-depth help for each option")
    if   'f' in sys.argv:
        parser.add_argument("fuzzy", nargs="?", help="No arguments necessary, however only ASCII terminals are supported")
    elif 'c' in sys.argv:
        parser.add_argument("i", nargs=(3), help="Verb information; Follows format: verb pronoun tense")
    elif 'a' in sys.argv:
        parser.add_argument("i", nargs=(2), help="Verb and tense for verb charts; If all tenses are required, use a in place of tense. \
            Follows format: verb tense")
    else:
        print("You did not provide a proper mode (f, c, or a), please try again with one of such arguments")
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
def modeVerstehen()->str:
    args = get_args()
    if args.mode[0] == "f":
        import fuzzy
        fuzzy.start()
    if args.mode[0] == "c":
        # TODO: from Deutschconjugation import conjugator as conj
        import conjugator as conj
        infinitive, pronoun, tense = lower_format()
        tense = tensePreprocessing(tense)
        z = conj.conjugate(infinitive, pronoun, tense)
        print(z)
    if args.mode[0] == "a":
        # TODO: from Deutschconjugation.conjugator import allesConjugate
        from conjugator import allesConjugate
        args = get_args()
        if args.i[1] == "alles" or args.i[1] == "a":
            tenses = ["present", "simple-past", "present-perfect", "past-perfect", "future"]
            allesConjugate(args.i[0], tenses)
        else:
            allesConjugate(args.i[0], [args.i[1]])

# Lower_case the args
def lower_format()->str:
    args = get_args()
    if len(args.i) < 3:
        raise("You are missing a few things")
        print("error")
    if len(args.i) > 3:
        raise("You have too many things")
    return args.i[0].lower(), args.i[1].lower(), args.i[2].lower()

# Conjugate and print args
def main()->str:
    modeVerstehen()

if __name__ != "__main__":
    import argparse

if __name__ == "__main__":
    import argparse
    main()