def verbreturns():
    return infinitives


if __name__ == "__main__" or __name__ != "__main__":
    import csv

    global infinitives
    global conjugations
    conjugations = []
    infinitives = []
    import os

    this_dir, this_filename = os.path.split(__file__)
    path = os.path.join(this_dir, "verbs.csv")
    with open(path, "r", newline="") as file:
        verblist = csv.reader(file)
        for row in verblist:
            try:
                infinitives.append(row[0])
            except:
                pass