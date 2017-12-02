#!/usr/bin/env python
import io

from setuptools import find_packages, setup


readme = io.open('README.rst', 'r', encoding='utf-8').read()

setup(
    name='shinydisco',
    description='Telnyx coding test',
    long_description=readme,
    author='Jacopo Cascioli',
    author_email='jacopocascioli@gmail.com',
    version='0.0.1',
    packages=find_packages(),
    tests_require=[
        'pytest>=3.3.0',
        'pytest-mock>=1.6.3'
    ],
    install_requires=[
        'click>=6.7'
    ],
    entry_points="""
        [console_scripts]
        shinydisco=shinydisco.Cli:Cli.main
    """
)
