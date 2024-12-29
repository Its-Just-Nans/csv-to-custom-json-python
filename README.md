# csv-to-custom-json-python [![pypi version](https://img.shields.io/pypi/v/csv-to-custom-json)](https://pypi.org/project/csv-to-custom-json/) ![pypi downloads](https://img.shields.io/pypi/dm/csv-to-custom-json)

- [PyPi page](https://pypi.org/project/csv-to-custom-json/)
- [PyPiStats](https://pypistats.org/packages/csv-to-custom-json)

## How to install

- [installation docs](https://github.com/Its-Just-Nans/csv-to-custom-json-python/tree/master/docs/How-to-install.md)

```sh
python3 -m pip install csv-to-custom-json
```

## Tests && coverage

Coverage is 100%

```sh
# install
python -m pip install coverage unittest

# only test
python -m unittest

# coverage
coverage run -m unittest  && coverage report -m
```

## How to use csv-to-custom-json

## Classic usage

Just import the function and use it !

```python
from csv_to_custom_json import parseFile

result = parseFile("myfile.csv")
```

## How to use the schema

Create a schema variable and put it as second parameter !

Example with a simple `csv` :

```csv
num1,num2,num3
1,2,3
4,5,6
7,8,9
```

```python
from csv_to_custom_json import parseFile

def callback(value):
    return None

schema = {
    "num1": "string",
    "num2": callback,
    "num3": "int"
}

result = parseFile("myfile.csv", schema)
```

> Caption :
>
> - ad you can see the schema can contains function, or string with the type
> - the values with type will be parsed
> - attribute of the object are the word in the first line of the csv

## More complexe schema

It's the same as a simple schema :

```python
from csv_to_custom_json import parseFile

schema = {
    "obj1": {
        "obj2": {
            "num4": "string"
        }
    },
    "num2": "",
    "num3": ""
}
result = parseFile("myfile.csv", schema)
```

If you want to check some real case, check out the folder `test` in the [GitHub repository](https://github.com/Its-Just-Nans/csv-to-custom-json-python)

If you want to see and use options check that documentation: [How-to-options](https://github.com/Its-Just-Nans/csv-to-custom-json-python/tree/master/docs/How-to-options.md)

## See also

- [Tricks](https://github.com/Its-Just-Nans/csv-to-custom-json-python/tree/master/docs/How-to-know-more.md)
- [How-to-options](https://github.com/Its-Just-Nans/csv-to-custom-json-python/tree/master/docs/How-to-options.md)
- [CHANGELOG.md](https://github.com/Its-Just-Nans/csv-to-custom-json-python/tree/master/CHANGELOG.md)
- [csv-to-custom-json in JavaScript](https://github.com/Its-Just-Nans/csv-to-custom-json)

## License

Licensed under the MIT License - [LICENSE](LICENSE)
