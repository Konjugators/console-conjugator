#!/usr/bin/env python3
"""
This application conjugates the verbs of multiple languages
Copyright (C) 2020 Konjugators
See LICENSE for more information
"""
import argparse
import platform
# TODO:
# from . import conjugator
# from . import fuzzy
# from . import version
import version
import conjugator
import fuzzy

def getColorAvailability()->bool:
    if platform.system() not in ['Linux', 'Darwin']: colors = False
    else: colors = True
    return colors

# Parse Args
def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        nargs=1,
        choices=["a", "c", "f", "v"],
        help="The conjugation functions that can be performed (f -> fuzzy, c -> conjugate, a -> all).",
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
            "infinitive", nargs=(1), help="infinitive: The infinitive of the verb.",
        )
        parser.add_argument(
            "pronoun", nargs=1, help="pronoun: The pronoun to be conjugated for. 'es' is not \
                currently supported (use 'er' instead).",
        )
        parser.add_argument(
            "tense", nargs=1, help="tense: The tense to be conjugated for. Only indikativ tenses, \
            not including Futur II or Imperative (to be added soon)",
        )
    elif "a" in current_mode:
        parser.add_argument(
            "infinitive", nargs=(1), help="infinitive: The infinitive of the verb.",
        )
        parser.add_argument(
            "tense", nargs=1, help="tense: The tense to be conjugated for. Use 'alles' to print \
            charts for every tense",
        )
    elif "v" in current_mode:
        print(f"console-conjugator version v{version.__version__}")
    else:
        raise argparse.ArgumentError(
            "You did not provide a proper mode (f, c, or a), please try again with one of such arguments",
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
        fuzzy.start()
    if args.mode[0] == "c":
        infinitive, pronoun, tense = lower_format()
        tense = tensePreprocessing(tense)
        z = conjugator.conjugate(infinitive, pronoun, tense, getColorAvailability())
        print(z)
    if args.mode[0] == "a":
        args = get_args()
        conjugator.allConjugate(args.infinitive[0], [args.tense[0]], getColorAvailability())


# Lower_case the args
def lower_format() -> str:
    args = get_args()
    return args.infinitive[0].lower(), args.pronoun[0].lower(), args.tense[0].lower()


# Conjugate and print args
def main() -> str:
    modeSelection()

if __name__ == "__main__":
    main()
