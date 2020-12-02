import unittest
import subprocess
import os, sys

z = os.path.join(os.getcwd())
sys.path.insert(1, z)

from Deutschconjugation.conjugator import conjugate


class TestSum(unittest.TestCase):

    # Using self-created methods instead of builtin

    # @staticmethod
    # def assertEqual(statement1, statement2)->None:
    #     assert statement1 == statement2, f"{statement1} was not found to be equivalent to {statement2}"

    # @staticmethod
    # def assertNotEqual(statement1, statement2)->None:
    #     assert statement1 == statement2, f"{statement1} was incorrectly found to be equivalent to {statement2}"

    def testNormalVerbs(self):
        verb_cases = {
            "machen": "er macht",
            "fahren": "er fährt",
            "spielen": "er spielt",
            "putzen": "er putzt",
            "haben": "er hat",
            # "sehen":"era"
        }

        for string in verb_cases.keys():
            conjugationResult = conjugate(str.strip(string), "er", "present")
            self.assertEqual(str.strip(verb_cases[string]), conjugationResult)


if __name__ == "__main__":
    unittest.main()
