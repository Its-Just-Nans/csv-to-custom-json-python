# Tricks

## Array Trick

If you have an simple array (not with object), the function can even parse your fields

```python
def my_func(allValues):
    return "hello"

schema = {
    "num1": [
        "num4",
        "text",
        my_func,
    ]
}
```

> Caption:
>
> - by default, `num4` in the firstLine will be parsed and replace by the corresponding value.
> - functions are in an array and can't be identified by a name, so we can't give to it a value parameter, so the function will receive an array with all value of the current line

## Array schema Trick

Fun-fact : schema can even be an array !

```python
def my_func(allValues):
    return "hello"
schema = [
    "num4",
    "text",
    my_func
]
```
