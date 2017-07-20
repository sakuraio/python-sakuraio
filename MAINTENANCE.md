# PyPi

Change version in `setup.py`.

## Testing

```bash
python setup.py sdist
twine upload dist/* -r pypitest
```

## Production

```bash
python setup.py sdist
twine upload dist/* -r pypi
```
