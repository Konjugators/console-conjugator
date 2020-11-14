def appverbs(z:list):
    with open("Ubersetzen/dict.csv", "a") as newverbs:
        csvWriter = csv.writer(newverbs, delimiter=",")
        csvWriter.writerows(z)

if __name__ == "__main__" or __name__ != "__main__":
    import csv
    import os
    this_dir, this_filename = os.path.split(__file__)