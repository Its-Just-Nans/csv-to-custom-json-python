# CHANGELOG

## Create a new version

```sh
rm -rf dist/ build/
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade build
python3 -m build
python3 -m pip install --upgrade twine
# create egg-info folder
python3 -m twine upload dist/* --verbose
# use __token__ auth
# enter token
```

## 2023-11-09

Use `pyproject.toml` instead of `setup.cfg`

## 2023-10-08

Better, remove `customSeparator`

## 2022-02-11

Add docs

## 2022-01-20

- first release : `https://pypi.org/project/csv-to-custom-json`
- note : [https://packaging.python.org/en/latest/tutorials/packaging-projects/](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- note : `python3 -m twine upload dist/*`

## 2021-12-08

Add option to pass a `list` as `schema`
