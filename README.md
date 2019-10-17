Semantic version implementation
============================================================

    pip install version==0.1.2

`Version` implements version object as described in
[Semantic Versioning spec 2.0.0-rc.1](http://semver.org).


Example of simple X.Y.Z version:

```python

>>> from semantic_version import SemanticVersion

>>> v = SemanticVersion('1.2.3')

>>> v
SemanticVersion('1.2.3')

>>> str(v)
'1.2.3'

>>> v.major
1

>>> v.minor
2

>>> v.patch
3

>>> v.pre_release
[]

>>> v.build
[]

```

Example with pre-release and build versions:


```python

>>> v2 = SemanticVersion('2.7.3-rc.2.15+19.e02afe3')

>>> v2.major
2

>>> v2.minor
7

>>> v2.patch
3

>>> v2.pre_release
['rc', 2, 15]

>>> v2.build
[19, 'e02afe3']

```

`SemanticVersion` supports rich comparison operators (<, <=, >, >=, ==, !=),
and thus can be sorted:

```python

>>> from __future__ import print_function
>>> versions = [SemanticVersion('1.0.0+0.3.7'),
...             SemanticVersion('1.0.0'),
...             SemanticVersion('1.0.0-beta.11'),
...             SemanticVersion('0.9.0'),
...             SemanticVersion('1.0.0-rc.1'),
...             SemanticVersion('1.0.0-rc.1+build.1'),
...             SemanticVersion('1.0.0-alpha.1')]

>>> print('\n'.join(map(str, sorted(versions))))
0.9.0
1.0.0-alpha.1
1.0.0-beta.11
1.0.0-rc.1
1.0.0-rc.1+build.1
1.0.0
1.0.0+0.3.7

```
