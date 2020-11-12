#!/usr/bin/env python3
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("infinitive", help="The unconjugated verb")

    parser.add_argument(
        "pronoun", help="The pronoun that the infinitve is being conjugated for"
    )

    parser.add_argument(
        "tense",
        help="The tense of the conjugated phrase in quotes if \
                    there are multiple words",
    )

    args = parser.parse_args()
    return args


def tensePreprocessing(tense: str) -> str:
    if tense in ["präsens"]:
        return "present"
    if tense in ["simplepast", "präteritum", "prateritum"]:
        return "simple-past"
    if tense in ["presentperfect", "perfekt"]:
        return "present-perfect"
    if tense in ["plusquamperfect", "pastperfect"]:
        return "past-perfect"
    if tense in ["zukunft"]:
        return "future"
    else:
        return tense


def lower_format():
    args = get_args()
    return args.infinitive.lower(), args.pronoun, args.tense.lower()


def main():
    from Deutschconjugation import conjugator as conj

    infinitive, pronoun, tense = lower_format()
    tense = tensePreprocessing(tense)
    z = conj.conjugate(infinitive, pronoun, tense)
    print(z)


if __name__ != "__main__":
    import argparse
