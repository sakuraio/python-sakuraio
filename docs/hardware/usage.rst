Getting Started
===============

Python-sakuraio provides a functions to execute command on Sakura Communication Modules.


Opening a interface
-------------------

Create instance for treat a Sakura Communication Module::

    from sakuraio.hardware.rpi import SakuraIOSMbus

    sakuraio = SakuraIOSMbus()


Examples
--------

Get the unique id of a Sakura Communication Module::

    >>> from sakuraio.hardware.rpi import SakuraIOSMbus
    >>> sakuraio = SakuraIOSMbus()
    >>> sakuraio.get_unique_id()
    "16X0000001"
