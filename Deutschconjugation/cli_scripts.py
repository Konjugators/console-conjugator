#!/usr/bin/env python3

import argparse
def main():
    args = get_args()
    from Deutschconjugation import conjugator
    infinitive, pronoun, tense = conjugator.format(args.infinitive), format(args.pronoun), format(args.tense)
    conj_out = f"{conjugator.conjugate(infinitive, pronoun, tense)}"
    print(conj_out)
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
    main()
    '''
    infinitive, pronoun, tense = to_lower_case()
<<<<<<< HEAD:Deutschconjugation/cli_scripts.py
    args= get_args()
=======

>>>>>>> fc142cb3677c31c5c022db5d9cf7664397c96778:Deutschconjugation/cli.py
    import conjugator
    from conjugator import format

    infinitive, pronoun, tense = format(infinitive), format(pronoun), format(tense)
    conj_out = f"\033[1;32;40m{conjugator.conjugate(infinitive, pronoun, tense)}\033[0m 1;34;40m"

    print(f"\033[1;34;40m{pronoun}\033[0m 1;34;40m {conj_out}")
    '''
