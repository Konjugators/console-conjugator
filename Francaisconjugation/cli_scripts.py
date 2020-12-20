import argparse
import platform
from Francaisconjugation import conjugator

def getColorAvailability() -> bool:
    if platform.system() not in ["Linux", "Darwin"]: colors = False
    else: colors = True
    return colors

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
    pass #TODO add cli