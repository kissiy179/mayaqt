#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from os.path import dirname, basename, splitext, exists
from glob import glob
from setuptools import setup

def _requires_from_file(filename):
    '''requirements.txtから必要パッケージを取得'''
    if not exists(filename):
        return []
    
    return open(filename).read().splitlines()

dir_path = dirname(__file__)
package_name = basename(dir_path)
module_names = [splitext(basename(path))[0] for path in glob(r'{}\python\*.py'.format(dir_path))]
requires_packages = _requires_from_file(r'{}\requirements.txt'.format(dir_path))

# セットアップ
setup(
    name=package_name,
    version='0.1.0',
    package_dir={"": "python"},
    py_modules=module_names,
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7",
    install_requires=[
    ]
)
