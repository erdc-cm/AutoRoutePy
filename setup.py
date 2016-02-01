# -*- coding: utf-8 -*-
##
##  setup.py
##  AutoRoutePy
##
##  Created by Alan D. Snow.
##  Copyright © 2015-2016 Alan D Snow. All rights reserved.
##  License: BSD-3 Clause

from setuptools import setup

setup(
    name='AutoRoutePy',
    version='0.0.1',
    description='Python scripting interface for the AutoRoute progam.'
                ' Has ability to Prepare input from RAPID output (www.rapid-hub.org).',
    keywords='AutoRoute',
    author='Alan Dee Snow',
    author_email='alan.d.snow@usace.army.mil',
    url='https://github.com/erdc-cm/AutoRoutePy',
    download_url='https://github.com/erdc-cm/AutoRoutePy/tarballs/0.0.1',
    license='BSD-3 Clause',
    packages=['AutoRoutePy'],
    install_requires=['condorpy', 'psutil', 'gdal', 'netCDF4'],
)
