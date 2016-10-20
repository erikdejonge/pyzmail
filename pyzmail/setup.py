#!/bin/env python
# pyzmail/setup.py
# (c) alain.spineux@gmail.com
# http://www.magiksys.net/pyzmail

import sys

if sys.version_info >= (3,):
    # distribute is required for py3k
    from distribute_setup import use_setuptools
    use_setuptools()

import sys, os, shutil

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

basename='pyzmail'
# retrieve $version
version=''
for line in open('pyzmail/version.py'):
    if line.startswith("__version__="):
        version=line[13:].rstrip()[:-1]
        break

if not version:
    print('!!!!!!!!!!!!!!!!!!!!!! VERSION NOT FOUND !!!!!!!!!!!!!!!!!!!!!!!!!')
    sys.exit(1)

print('VERSION', version)

extra_options = {}
doc_dir='share/doc/%s-%s' % (basename, version)

cmdclass = {}
data_files=[ ]

data_files.append( (doc_dir, [ 'README.txt', 'Changelog.txt', 'LICENSE.txt']) )

# support for python 3.x with "distribute"
if sys.version_info >= (3,):
    # avoid setuptools to report unknown options under python 2.X
    extra_options['use_2to3'] = True
    # extra_options['convert_2to3_doctests'] = ['src/your/module']
    # extra_options['use_2to3_fixers'] = ['your.fixers' ]
    extra_options['install_requires']=['distribute'], # be sure we are using distribute

setup(name='pyzmail',
      version=version,
      author='Alain Spineux',
      author_email='alain.spineux@gmail.com',
      url='http://www.magiksys.net/pyzmail',
      keywords= 'email',
#      maintainer = 'email', #
      description='Python easy mail library, to parse, compose and send emails',
      long_description='pyzmail is a high level mail library for Python 2.x & 3.x. '
                       'It provides functions and classes that help to parse, '
                       'compose and send emails. pyzmail exists because their '
                       'is no reasons that handling mails with Python would '
                       'be more difficult than with Outlook or Thunderbird. '
                       'pyzmail hide the difficulties of managing the MIME '
                       'structure and of the encoding/decoding for '
                       'internationalized emails. '
                       'pyzmail is well documented, has a lot of code samples '
                       'and include 2 scripts: pyzsendmail and pyzinfomail',
      license='LGPL',
      packages=[ 'pyzmail', 'pyzmail.tests' ],
      test_suite = 'pyzmail.tests',
      scripts=[ 'scripts/pyzsendmail', 'scripts/pyzinfomail' ],
      data_files=data_files,
      classifiers=["Intended Audience :: Developers",
                  "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
                  "Operating System :: OS Independent",
                  "Topic :: Communications :: Email",
                  "Topic :: System :: Networking",
                  "Topic :: Internet",
                  "Intended Audience :: Developers",
                  "Programming Language :: Python",
                  "Programming Language :: Python :: 2",
                  "Programming Language :: Python :: 3",
                  ],
      cmdclass = cmdclass,
      **extra_options)

if 'sdist' in sys.argv and 'upload' in sys.argv:
    print("After an upload, don't forget to change 'maintainer' to 'email' to be hight in pypi index")
