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


if __name__ == "__main__":
    infinitive, pronoun, tense = to_lower_case()
    
    import conjugator
    from conjugator import format
    infinitive, pronoun, tense = format(infinitive), format(pronoun), format(tense)

    print(f"{pronoun} {conjugator.conjugate(infinitive, pronoun, tense)}")
