# Python library for SakuraIO ![travis-ci](https://travis-ci.org/sakura-internet/python-sakuraio.svg?branch=master)

**WARNING: This library is under development with destructive changes.**

## Overview

This library contains two functions.
One is to connect to Sakura Communication Modules (for Hardware).
Another one is to connect to Platform API in https://api.sakura.io/ (for Service).


## Documentation

For API documentation, usage and examples see files in the `"./doc"`
directory.  The `".rst"` files can be read in any text editor or being converted to
HTML or PDF using [Sphinx](http://sphinx-doc.org/). An HTML version is online at

[![Docs](https://readthedocs.org/projects/python-sakuraio/badge/?version=latest)](http://python-sakuraio.readthedocs.io/)

http://python-sakuraio.readthedocs.io/


## For Hardware

It currently supports I2C (SMBus) ONLY, and tested with Raspberry Pi.


### Requirements

* Python >= 3.4
* python3-smbus (for I2C)
* python3-rpi.gpio (for GPIO on Raspberry Pi)

### Install

```bash
# From PyPi
sudo pip3 install sakuraio
# From Github.com
sudo pip3 install -e git+https://github.com/sakura-internet/python-sakuraio.git#egg=sakuraio
```

### Example

#### I2C (SMBus)

```python
from sakuraio.hardware.rpi import SakuraIOSMBus

sakuraio = SakuraIOSMBus()
print(sakuraio.get_unique_id())
```

#### SPI (GPIO)

```python
from sakuraio.hardware.rpi import SakuraIOGPIO

sakuraio = SakuraIOGPIO()
print(sakuraio.get_unique_id())
```


#### output

```
16X0000001
```
