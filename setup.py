#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

import performance_tools

with open('requirements.txt', 'r') as f:
    requires = f.read().splitlines()


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = ''

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        errno = tox.cmdline(args=shlex.split(self.tox_args))
        sys.exit(errno)


setup(
    name='ebury-elastic',
    version=performance_tools.__version__,
    description=performance_tools.__description__,
    long_description='\n'.join([open('README.rst').read(), open('CHANGELOG').read()]),
    author=performance_tools.__author__,
    author_email=performance_tools.__email__,
    url=performance_tools.__url__,
    packages=[
        'performance_tools',
    ],
    include_package_data=True,
    install_requires=requires,
    license=performance_tools.__license__,
    zip_safe=False,
    keywords='python, django, performance, measure, time, request, graph, analysis',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    test_suite='tests',
    tests_require=['tox'],
    cmdclass={'test': Tox},
)
