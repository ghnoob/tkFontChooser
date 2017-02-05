"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='tkFontChooser',
    version='1.0.0',
    description='A simple font chooser for Tkinter',
    long_description=long_description,
    url='https://pypi.python.org/pypi/tkFontChooser',
    author='Juliette Monsel',
    author_email='j_4321@protonmail.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Natural Language :: English',
        'Natural Language :: French',
        'Operating System :: OS Independent',
    ],

    keywords=['tkinter', 'font', 'fontchooser'],
    py_modules=["tkFontChooser"],

)