#!/usr/bin/env python

from distutils.core import setup

setup(
    name='SakuraIO',
    version='0.1.6',
    description='Python sakura.io Library',
    author='chibiegg',
    author_email='y-egusa@sakura.ad.jp',
    url='https://github.com/sakuraio/python-sakuraio/',
    packages=[
        'sakuraio',
        'sakuraio.hardware',
        'sakuraio.hardware.commands',
        'sakuraio.hardware.rpi',
        'sakuraio.software',
        'sakuraio.software.apis'
    ],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',
        # Indicate who your project is intended for
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Hardware',
        'Topic :: Utilities',
        'Topic :: Communications',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
