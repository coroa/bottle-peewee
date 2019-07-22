#!/usr/bin/env python

import os
from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

filename = os.path.join(os.path.dirname(__file__), 'bottle_peewee.py')
source = open(filename).read().split('### CUT HERE')[0]
exec(source)

setup(
    name='bottle-peewee',
    version='0.1',
    url='https://github.com/oz123/bottle-peewee',
    description='Peewee integration for Bottle.',
    long_description=__doc__,
    author='Oz Tiram',
    author_email='oz.tiram',
    license='MIT',
    platforms='any',
    py_modules=[
        'bottle_peewee'
    ],
    requires=[
        'bottle>=0.12',
        'peewee>=3.0'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    cmdclass={'build_py': build_py}
)
