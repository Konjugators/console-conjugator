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


def to_lower_case():
    args = get_args()
    return args.infinitive.lower(), args.pronoun.lower(), args.tense.lower()


def main():
    args = get_args()
    from Deutschconjugation import conjugator

    infinitive, pronoun, tense = (
        conjugator.format(args.infinitive),
        format(args.pronoun),
        format(args.tense),
    )
    conj_out = f"\033[34m{conjugator.conjugate(infinitive, pronoun, tense)}\033[0m"

    print(f"\033[32m{pronoun}\033[0m{conj_out}")


if __name__ == "__main__":
    main()
