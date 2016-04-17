#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup, Extension

mod_inject = Extension('pyinjectcode',
                       sources = ['pyinjectcode.c'])

setup (name = 'pydbattach',
       version = '1.0',
       description = 'attach to running Python process',
       ext_modules = [mod_inject])

# python setup.py build_ext --inplace
