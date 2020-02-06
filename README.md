# Versioning Package

The versioning package is a fork from the [version](https://pypi.org/project/version/) package which implements semantic versioning. The primary reason for forking [version](https://pypi.org/project/version/) is to extend functionality to support a non-semantic versioning schema.

    pip install enhanced-versioning==0.2.1

## Semantic version implementation

The `Enhanced-Versioning` package provides `SemanticVersion` which implements versioning as described in [Semantic Versioning spec 2.0.0-rc.1](http://semver.org).


Example of simple X.Y.Z version:

```python

>>> from enhanced_versioning import SemanticVersion

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

## Non-Semantic version implementation

The `Versioning` package provides `NonSematicVersion` which implements a non-semantic versioning system as described below.

### Non-Semantic Versioning Specification

This specification carries over much of the Sematic Versioning Specification except as noted.
1. Software using Non-Semantic Version MAY declare a public API, but it is not required.
2. A version MUST consist of one or more dot separated revisions. A revision MUST contain at least one non-negative integer or ASCII alphabetical character [0-9A-Za-z] in which integers, if present, must precede characters. The revision is treated as two parts. The integer value and the character value where the integer value takes precedence over the character value in comparisons. Each revision much increase. For instance: 1.2a.4 -> 1.2b.4 -> 1.3a.4.
3. See [Semantic Versioning Specification Rule 3](https://semver.org)
4. Non-Semantic Versioning does not define a standard for stability.
5. Non-Semantic Versioning does not require a public API to be defined.
6. Revisions to the left MUST carry greater weight than revisions to the right, but Non-Semantic Versioning does not define precisely what each revision must mean.
7. Revisions to the right MUST be reset to the appropriate beginning value when revisions to the left are incremented. The integer value of a revision MUST be reset to 0. The character value SHOULD be reset to 'a'.
8. See rule 7 above.
9. See [Semantic Versioning Specification Rule 9](https://semver.org) regarding pre-releases.
10. See [Semantic Versioning Specification Rule 10](https://semver.org) regarding builds.
11. Precedence MUST be calculated by separating individual revisions and pre-release identifiers. Precedence is determined first by the number of revisions with more revisions taking precedence over fewer. If the number of revisions is equal, then precedence is determined by the first difference when comparing revisions from left to right where the integer values of the revisions are compared numerically first followed by the character values compared alphabetically. Example: 1 < 1.0 < 1.1a < 1.1e < 1.2a. When all revisions are equal, the precedence must be determined by pre-releases. See [Semantic Versioning Specification Rule 11](https://semver.org) for full details on pre-release precedence.

Example of non-semantic versioning:

```python

>>> from enhanced_versioning import NonSemanticVersion

>>> v = NonSemanticVersion('1')

>>> v
NonSemanticVersion('1')


>>> str(v)
'1'

>>> v.revisions
['1']

>>> v.pre_release
[]

>>> v.build
[]

```
Example with pre-release and build versions:


```python

>>> v2 = NonSemanticVersion('1.4f.2c-rc.2.15+19.e02afe3')

>>> v2
NonSemanticVersion('1.4f.2c-rc.2.15+19.e02afe3')


>>> str(v2)
'1.4f.2c-rc.2.15+19.e02afe3'

>>> v2.revisions
['1', '4f', '2c']

>>> v2.pre_release
['rc', 2, 15]

>>> v2.build
[19, 'e02afe3']

```

`NonSemanticVersion` supports rich comparison operators (<, <=, >, >=, ==, !=),
and thus can be sorted:

```python

>>> versions = [NonSemanticVersion('1.0.4d.7f+0.3.7'),
...             NonSemanticVersion('1.0.4d.7f'),
...             NonSemanticVersion('1.0.4d.7f-beta.11'),
...             NonSemanticVersion('0.9.4d.7f'),
...             NonSemanticVersion('1.0.4d.7f-rc.1'),
...             NonSemanticVersion('1.0.4d.7f-rc.1+build.1'),
...             NonSemanticVersion('1.0.4d.7f-alpha.1'),
...             NonSemanticVersion('1.0.2f.12k+build.3')]

>>> print('\n'.join(map(str, sorted(versions))))
0.9.4d.7f
1.0.2f.12k+build.3
1.0.4d.7f-alpha.1
1.0.4d.7f-beta.11
1.0.4d.7f-rc.1
1.0.4d.7f-rc.1+build.1
1.0.4d.7f
1.0.4d.7f+0.3.7

```
