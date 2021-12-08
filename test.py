from main import parseFile
from json import dumps as JSONstringify

schema = {
    "test1": [
        "test3"
    ],
    "test2": "string"
}

schema2 = {
    "test1": {
        "test3": "string",
    },
    "test2": "string"
}

schema3 = [
    "test1",
    {
        "test4": "string",
    },
    "test2"
]


def test(parsedLine=[], a=[]):
    return None


options = {
    "lineCallBack": test
}

res = parseFile("csv.txt", {}, options)

print(JSONstringify(res, indent=4))
