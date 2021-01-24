import unittest
import subprocess
import os, sys

z = os.path.join(os.getcwd())

# Be able to access Deutschconjugation module locally
sys.path.insert(1, z)

from Conjugator.Deutschconjugation.conjugator import conjugate


class TestSum(unittest.TestCase):
    def testErPresentVerbs(self):
        verb_cases = {
            "machen": "er macht",
            "fahren": "er fährt",
            "spielen": "er spielt",
            "putzen": "er putzt",
            "haben": "er hat",
        }

        for string in verb_cases.keys():
            conjugationResult = conjugate(str.strip(string), "er", "present")
            self.assertEqual(str.strip(verb_cases[string]), conjugationResult)

    def testIchPresentVerbs(self):
        verb_cases = {
            "machen": "ich mache",
            "fahren": "ich fahre",
            "spielen": "ich spiele",
            "putzen": "ich putze",
            "haben": "ich habe",
        }

        for string in verb_cases.keys():
            conjugationResult = conjugate(str.strip(string), "ich", "present")
            self.assertEqual(str.strip(verb_cases[string]), conjugationResult)


if __name__ == "__main__":
    unittest.main()
