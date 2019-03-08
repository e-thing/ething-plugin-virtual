
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# io.open is needed for projects that support Python 2.7
# It ensures open() defaults to text mode with universal newlines,
# and accepts an argument to specify the text encoding
# Python 3 only projects can skip this import
from io import open
import json
from os.path import join, dirname, abspath


here = abspath(dirname(__file__))

NAME = 'ething_plugin_virtual'

# Get the long description from the README file
with open(join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='ething-plugin-virtual',

    version='0.0.1',

    description='ething plugin virtual',

    long_description=long_description,

    long_description_content_type='text/markdown',

    keywords='ething plugin virtual',

    packages=[NAME],

    install_requires=[
        'ething'
    ],
)
