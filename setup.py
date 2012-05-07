#!/usr/bin/env python
# Namespace Trie
# Copyright (C) 2012  Paul Horn
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__author__ = 'knutwalker@gmail.com (Paul Horn)'


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='namespacetrie',
    version='0.1',
    description=('A Trie implementation that manages not the single characters'
                 ' but treats its values as typical namespaces.'),
    license='GPLv3',
    author='Paul Horn',
    author_email='knutwalker@gmail.com',
    url='https://github.com/knutwalker/namespacetrie',

    keywords = "namespace trie",
    long_description="""
This is the Namespace Trie.

Namespace Trie is a implementation of a Trie data structure.  Unlike typical
implementations, which are splitting its value into single characters,
Namespace Trie treats its values as namespaces.  Namespaces are strings that
are delimited by a period. Such namespaces often occur in programming
languages, e.g. Java or Python and may also appear while using some libraries
for programming languages that itself do not offer namespacing (e.g. the
Google Closure library offers a namespace feature for JavaScript).  The
Namespace Trie may help you find flaws in the namespace structure.

Namespace Trie is developed for use with Closure Depresolver and may at the
moment not be very useful as there is not standalone interface.
    """.strip(),

    install_requires=['weakrefset', 'ordereddict'],

    package_dir={'namespacetrie': 'namespacetrie'},
    packages=['namespacetrie'],

    test_suite="namespacetrie.nstrie_test"
)
