#!/usr/bin/env python3
"""
This application conjugates the verbs of multiple languages
Copyright (C) 2020 Konjugators
See LICENSE for more information
"""
import argparse
import platform

def getColorAvailability():
    if platform.system() not in ['Linux', 'Darwin']: colors = False
    else: colors = True
    return colors

# Parse Args
def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        nargs=1,
        choices=["a", "c", "f"],
        help="The conjugation functions that can be performed (f -> fuzzy, c -> conjugate, a -> all). \
        Add the -h flag after selecting a mode to see in-depth help for each option",
    )
    current_mode = vars(parser.parse_known_args()[0])['mode'];
    if "f" in current_mode:
        parser.add_argument(
            "fuzzy",
            nargs="?",
            help="No arguments necessary, may not work on a Windows",
        )
    elif "c" in current_mode:
        parser.add_argument(
            "i", nargs=(3), help="Verb information; Follows format: verb pronoun tense"
        )
    elif "a" in current_mode:
        parser.add_argument(
            "i",
            nargs=(2),
            help="Verb and tense for verb charts; If all tenses are required, use a in place of tense. \
            Follows format: verb tense",
        )
    else:
        raise argparse.ArgumentError(
            "You did not provide a proper mode (f, c, or a), please try again with one of such arguments"
        )
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
def modeSelection() -> str:
    args = get_args()
    if args.mode[0] == "f":
        # TODO:
        # from Deutschconjugation import fuzzy
        from . import fuzzy

        # import fuzzy

        fuzzy.start()
    if args.mode[0] == "c":
        # TODO: 
        # from Deutschconjugation import conjugator as conj
        from . import conjugator
        # from conjugator import conjugate

        infinitive, pronoun, tense = lower_format()
        tense = tensePreprocessing(tense)
        z = conjugator.conjugate(infinitive, pronoun, tense, getColorAvailability())
        print(z)
    if args.mode[0] == "a":
        # TODO: 
        # from Deutschconjugation.conjugator import allConjugate
        from . import conjugator
        # from conjugator import allConjugate

        args = get_args()
        conjugator.allConjugate(args.i[0], [args.i[1]], getColorAvailability())


# Lower_case the args
def lower_format() -> str:
    args = get_args()
    if len(args.i) < 3:
        raise ("You are missing a few arguments")
    if len(args.i) > 3:
        raise ("You have given too many arguments")
    return args.i[0].lower(), args.i[1].lower(), args.i[2].lower()


# Conjugate and print args
def main() -> str:
    modeSelection()

if __name__ == "__main__":
    main()
