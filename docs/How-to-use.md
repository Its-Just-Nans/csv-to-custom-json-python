# How to use csv-to-custom-json

## Classic usage

Just import the function and use it !

```python
from csv_to_custom_json import parseFile

result = parseFile("myfile.csv")
```

## How to use the schema

Create a schema variable and put it as second parameter !

Exemple with a simple `csv` :

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
    num1: "string",
    callback,
    num3: "int"
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
    obj1: {
        obj2: {
            num4: "string"
        }
    },
    num2: "",
    num3: ""
}
result = parseFile("myfile.csv", schema)
```

If you want to check some real case, check out the folder `test` in the [GitHub repository](https://github.com/Its-Just-Nans/csv-to-custom-json-python)

If you want to see and use options check that documentation : [How-to-options](https://github.com/Its-Just-Nans/csv-to-custom-json-python/wiki/How-to-options)
