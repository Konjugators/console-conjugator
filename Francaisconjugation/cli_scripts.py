import argparse
import platform
from Francaisconjugation import conjugator as conj


def getColorAvailability() -> bool:
    return platform.system() in ("Linux", "Darwin")


def get_args() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "mode",
        nargs=1,
        choices=["a", "c", "f", "v"],
        help="The conjugation functions that can be performed (f -> fuzzy, c -> conjugate, a -> all).",
    )
    args = parser.parse_args()
    return args


def main():
    pass  # TODO add cli
