from main import parseFile

schema = {
    "test1": {
        "test3": "string",
    },
    "test2": "string"
}


def test(parsedLine=[], a=[]):
    return None


options = {
    "lineCallBack": test
}

res = parseFile("csv.txt", schema, options)

print(res)
