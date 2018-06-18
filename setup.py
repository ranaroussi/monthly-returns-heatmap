#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Monte Carlo Simulator for Pandas
# https://github.com/ranaroussi/pandas-montecarlo

"""Monte Carlo Simulator for Pandas"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='monthly-returns-heatmap',
    version="0.0.9",
    description='Utility to create a monthly returns heatmap from Pandas series',
    long_description=long_description,
    url='https://github.com/ranaroussi/monthly-returns-heatmap',
    author='Ran Aroussi',
    author_email='ran@aroussi.com',
    license='LGPL',
    classifiers=[
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Development Status :: 5 - Production/Stable',

        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    platforms = ['any'],
    keywords='plot, heatmap, returns grid',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['pandas', 'matplotlib', 'seaborn'],
    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
