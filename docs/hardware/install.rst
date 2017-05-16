Installation
============

Python-sakuraio can be installed from Github.com with tools like ``pip``:

.. code-block:: bash

    # From PyPi
    $ pip install sakuraio
    # From Github.com
    $ pip install -e git+https://github.com/sakuraio/python-sakuraio.git#egg=sakuraio


Requirements
------------

Python-sakuraio is tested on Python >= 3.4,


Raspberry Pi
~~~~~~~~~~~~

Python-sakuraio is tested against all supported versions of Raspberry Pi and
`Raspbian`__ with Raspberry Pi.

__ https://www.raspberrypi.org/downloads/raspbian/

* **Raspberry Pi**: 3, Zero
* **Raspbian**: Raspbian Jessie 2017-03-02

.. code-block:: bash

    $ sudo apt-get install python3 python3-pip python3-smbus
    $ pip3 install -e git+https://github.com/sakuraio/python-sakuraio.git#egg=sakuraio
