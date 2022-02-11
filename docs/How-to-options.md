# How to use csv-to-custom-json-python options

## Options

To use options, you need to add a third parameters which is an object with options.

Example :

```python
parsedFile = parseFile("myfile.csv", schema, {
    debug: True
})
```

## Informations for tests

- For options, when it is written `boolean`, in reality, it can be any `True` value of python. Same for `False`.

- command to run test

```sh
python3 -m unittest
```

---

### Debug

> - name: `debug`
> - default: `False`
> - value: boolean: `True` or `False`

This options show the parsed result of your schema (can be useful sometimes)

This options also allow log from the function (example, a mistake)

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_debug.py
```

</details>

---

### Separator

> - name: `separator`
> - default: `,`
> - values: string

`.csv` stands for "Comma Separated Values", but if you're a rebel, this options is made for you :)

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_custom_separator.py
```

</details>

---

### Parse

> - name: `parse`
> - default: `True`
> - value: boolean: `True` or `False`

This function deactivates the parsing of values: `function`, `int`, `float`, `string`

With this function all is string

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_stop_parse_value.py
```

</details>

---

### Line Call Back

> - name: `lineCallBack`
> - default: `null`
> - value: function (async or not)

It activates the callBack after each line, can be useful if ou want to do a insert in database (for example)

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_line_callBack.py
python3 -m unittest tests/test_line_callBack_force.py
python3 -m unittest tests/test_line_callBack_value.py
```

</details>

---

### Call Back Force

> - name: `callBackForce`
> - default: `False`
> - value: boolean: `True` or `False`

This options allow you to force taking the result of the callBackLine even if it's `undefined` or `null`

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_callBack_force.py
python3 -m unittest tests/test_callBack_force_2.py
```

</details>

---

### Array Parse

> - name: `arrayParse`
> - default: `True`
> - value: boolean: `True` or `False`

This options allow you to disable the parsing in an array.

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_array_parse.py
```

</details>

---

### Override First Line

> - name: `overrideFirstLine`
> - default: `False`
> - value: `array of string` or `False`

This options allow you to override the first line.

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_override_first_line.py
```

</details>

### Private separator

> - name: `privateSeparator`
> - default: `...`
> - value: `string`

This options allow you to change the internal separator of the script. It can be useful if values contain `.` in their names

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_private_separator.test.js test/private_separator_2.py
```

</details>

### Avoid void line

> - name: `avoidVoidLine`
> - default: `False`
> - value: `boolean`

This options allow you to not parse void line

<details>
<summary>Test</summary>

```sh
python3 -m unittest tests/test_avoidVoidLine.test.js tests/avoidVoidLine2.test.js tests/test_avoidVoidLine3.py
```

</details>
