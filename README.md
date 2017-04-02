# Python library for SakuraIO

## For Sakrura Communication Module

Currently supports I2C (SMBus) ONLY.


### Requirements

* Python >= 3.5
* python3-smbus (for I2C)


### Install

```bash
sudo pip3 install -e git+https://github.com/sakura-internet/python-sakuraio.git#egg=python-sakuraio
```

### Example

```python
from sakuraio.hardware.rpi import SakuraIOSMBus

sakuraio = SakuraIOSMBus()
print(sakuraio.get_unique_id())
```

#### output

```
16X0000001
```
