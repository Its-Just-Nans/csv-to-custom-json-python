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


def add(n):
    return n+n


a = {
    "lol": "mdr",
    "a": add
}
print(a["a"](1))

test = [1, 2]
test_b = [3]
test_b = [*test, *test_b, 3]
print(test_b)
