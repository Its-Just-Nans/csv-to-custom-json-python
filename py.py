from csv import reader

options = {
    "separator": ","
}
with open("csv.txt") as csv_file:
    lineReader = reader(csv_file, delimiter=options["separator"])
    firstLine = next(lineReader)
    print(firstLine)
    print("sqdgqsgdg")
    for row in lineReader:
        print(row)