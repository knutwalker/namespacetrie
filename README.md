[![Build Status](https://secure.travis-ci.org/knutwalker/namespacetrie.png?branch=master)](http://travis-ci.org/knutwalker/namespacetrie)

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

This file was modified by PyCharm 2.5 for binding GitHub repository



## Install

from pip:

    pip install namespacetrie

from source:

    pip install git+git://github.com/knutwalker/namespacetrie.git


## Usage

```python
from namespacetrie.nstrie import NsTrie
modules = ['com.example.foo', 'com.example.bar', 'com.example.baz.Foo',
           'com.example.baz.Bar', 'org.example']
trie = NsTrie(modules)
'com.example' in trie
# True

trie.has('com.example')
# False

trie.has('com.example', False)
# True

trie.has('com.example.foo')
# True

node = trie.get('com.example')
node.keys()
# ['foo', 'bar', 'baz']

trie.to_dict()
# {'com': {'example': {'bar': 'com.example.bar',
#    'baz': {'Bar': 'com.example.baz.Bar', 'Foo': 'com.example.baz.Foo'},
#    'foo': 'com.example.foo'}},
#  'org': {'example': 'org.example'}}

list(trie.iterdepth())
# ['com', 'com.example', 'com.example.foo', 'com.example.bar',
#  'com.example.baz', 'com.example.baz.Foo', 'com.example.baz.Bar',
#  'org', 'org.example']

list(trie.iterbreadth())
# ['com', 'org', 'com.example', 'org.example', 'com.example.foo',
#  'com.example.bar', 'com.example.baz', 'com.example.baz.Foo',
#  'com.example.baz.Bar']

trie.remove('com')
list(trie)
# [('org', [('example', 'org.example')])]
```
