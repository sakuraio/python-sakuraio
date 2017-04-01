#!/usr/bin/env python

from distutils.core import setup

setup(
    name='SakuraIO',
    version='1.0',
    description='Python SakuraIO Library',
    author='chibiegg',
    author_email='chibiegg@chibiegg.net',
    url='https://iot.sakura.ad.jp/',
    packages=['sakuraio', 'sakuraio.hardware', 'sakuraio.hardware.commands', 'sakuraio.hardware.rpi'],
)
