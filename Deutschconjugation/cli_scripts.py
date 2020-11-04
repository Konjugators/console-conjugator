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
    # don't change case of pronoun
    # to avoid conflating Sie and sie
    return args.infinitive.lower(), args.pronoun(), args.tense.lower()


def main():
    import os
    print(os.getcwd())
    args = get_args()
    import conjugator

    def conj(arg1, arg2, arg3):
        return conjugator.conjugate(arg1, arg2, arg3)

    if args.pronoun != "alles" and args.tense != "alles":
        infinitive, pronoun, tense = (
            conjugator.format(args.infinitive),
            format(args.pronoun),
            format(args.tense),
        )

    def proalles(tense):
        things = ["ich", "wir", "Sie", "du", "ihr", "er", "sie"]
        inf = args.infinitive
        str = f"| ich {conj(inf, things[0], tense)} | wir {conj(inf, things[1], tense)} | Sie {conj(inf, things[2], tense)} |"
        ste = f"| du  {conj(inf, things[3], tense)} | ihr {conj(inf, things[4], tense)} | "
        sty = (
            f"| er  {conj(inf, things[5], tense)} | sie {conj(inf, things[6], tense)} |"
        )
        start = "_" * len(str)
        stop = "‾" * len(sty)
        mid = "-" * len(str)
        midagain = "-" * len(ste)
        print(start, str, mid, ste, midagain, sty, stop, sep="\n")
        return 0

    if args.pronoun == "alles" and args.tense != "alles":
        proalles(args.tense)
    if args.tense == "alles" and args.pronoun != "alles":
        for i in ["present", "present-perfect", "simple-past", "future", "imperative"]:
            print(f"{i}: {conj(args.infinitive, args.pronoun, i)}", end="\n")
        return 0
    if args.tense == "alles" and args.pronoun == "alles":
        for k in ["present", "present-perfect", "simple-past", "future", "imperative"]:
            print(k + ": ")
            proalles(k)
        return 0

    import platform

    if args.tense != "alles" and args.pronoun != "alles":
        if platform.system() != "Windows":
            conj_out = (
                f"\033[34m{conjugator.conjugate(infinitive, pronoun, tense)}\033[0m"
            )
            print(f"\033[32m{pronoun}\033[0m {conj_out}")
        else:
            print(f"{pronoun} {conjugator.conjugate(infinitive, pronoun, tense)}")


if __name__ == "__main__":
    main()
