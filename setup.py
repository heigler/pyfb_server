#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='pyfb_server',
    version='0.1',
    description='A simple python http server with Facebook behaviour.',
    author='Heigler Rocha',
    author_email='lordheigler@gmail.com',
    long_description=open('README.md', 'r').read(),
    packages=[
        'pyfb_server'
    ],
    classifiers=[
        'Development Status :: 1 - Alpha/not stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)