"""Base version class"""
import sys
import re

if sys.version_info >= (3, 0):
    from itertools import zip_longest as izip_longest
else:
    from itertools import izip_longest


class _Comparable(object):
    """Rich comparison operators based on __lt__ and __eq__."""

    __gt__ = lambda self, other: not self < other and not self == other
    __le__ = lambda self, other: self < other or self == other
    __ne__ = lambda self, other: not self == other
    __ge__ = lambda self, other: self > other or self == other


class VersionError(Exception):
    pass


class _Seq(_Comparable):
    """Sequence of identifies that could be compared according to semver."""

    def __init__(self, seq):
        self.seq = seq

    def __lt__(self, other):
        assert set([int, str]) >= set(map(type, self.seq))
        for s, o in izip_longest(self.seq, other.seq):
            assert not (s is None and o is None)
            if s is None or o is None:
                return bool(s is None)
            if type(s) is int and type(o) is int:
                if s < o:
                    return True
            elif type(s) is int or type(o) is int:
                return type(s) is int
            elif s != o:
                return s < o

    def __eq__(self, other):
        return self.seq == other.seq


class BaseVersion(_Comparable):
    """ Base version class """
    REVISION_DELIMITER = '.'
    PRE_RELEASE_DELIMITER = '-'
    BUILD_DELIMITER = '+'

    def __init__(self, *args, **kwargs):
        raise NotImplementedError('%s cannot be instantiated.' % self.__class__.__name__)

    def __str__(self):
        s = self.REVISION_DELIMITER.join(self._str_rev(rev) for rev in self._revisions())
        if self.pre_release:
            s += self.PRE_RELEASE_DELIMITER + self.REVISION_DELIMITER.join(str(s) for s in self.pre_release)
        if self.build:
            s += self.BUILD_DELIMITER + self.REVISION_DELIMITER.join(str(s) for s in self.build)
        return s

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.__str__())

    def __lt__(self, other):
        self._assume_to_be_comparable(other)
        if self._revisions() == other._revisions():
            if self.pre_release == other.pre_release:
                if self.build == other.build:
                    return False
                elif self.build and other.build:
                    return _Seq(self.build) < _Seq(other.build)
                elif self.build or other.build:
                    return bool(other.build)
                assert not 'reachable'
            elif self.pre_release and other.pre_release:
                return _Seq(self.pre_release) < _Seq(other.pre_release)
            elif self.pre_release or other.pre_release:
                return bool(self.pre_release)
            assert not 'reachable'
        return self._revisions() < other._revisions()

    def __eq__(self, other):
        self._assume_to_be_comparable(other)
        return all([self._revisions() == other._revisions(),
                    self.build == other.build,
                    self.pre_release == other.pre_release])

    def _assume_to_be_comparable(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('cannot compare `%r` with `%r`' % (self, other))

    def _make_group(self, g):
        return [] if g is None else list(map(self._try_int, g[1:].split(self.REVISION_DELIMITER)))

    @staticmethod
    def _try_int(s):
        assert isinstance(s, str)
        try:
            return int(s)
        except ValueError:
            return s

    @staticmethod
    def _str_rev(rev):
        return str(rev)
