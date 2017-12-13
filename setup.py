#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


setup(
    name     = 'djchoices',
    version  = '1.0.0',

    author       = 'orsinium',
    author_email = 'master_fess@mail.ru',

    description  = 'Choices for Django.',
    long_description = open('README.md').read(),
    keywords     = 'django choices choice autocomplete',

    packages = ['djchoices'],
    requires = ['python (>= 2.4)'],

    url          = 'https://github.com/orsinium/djchoices',
    download_url = 'https://github.com/orsinium/djchoices/tarball/master',

    license      = 'GNU Lesser General Public License v3.0',
    classifiers  = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Programming Language :: Python',
    ],
)
