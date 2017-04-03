# PyPi

## Testing

```bash
python setup.py register -r https://testpypi.python.org/pypi
python setup.py sdist upload -r https://testpypi.python.org/pypi
```

## Production

```bash
python setup.py register
python setup.py sdist upload
```
