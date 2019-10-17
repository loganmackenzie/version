from __future__ import print_function
import sys
import re

if sys.version_info >= (3, 0):
    from itertools import zip_longest as izip_longest
else:
    from itertools import izip_longest


from base_version import BaseVersion, VersionError

_re = re.compile('^'
                 '(\d+)\.(\d+)\.(\d+)'  # minor, major, patch
                 '(-[0-9A-Za-z-\.]+)?'  # pre-release
                 '(\+[0-9A-Za-z-\.]+)?'  # build
                 '$')


class SemanticVersion(BaseVersion):
    """ Manage semantic versions """
    def __init__(self, version, strict=True):
        match = _re.match(version)
        if not match:
            raise VersionError('invalid version %r' % version)
        self.major, self.minor, self.patch = map(int, match.groups()[:3])
        self.pre_release = self._make_group(match.group(4))
        self.build = self._make_group(match.group(5))

    def _revisions(self):
        return [self.major, self.minor, self.patch]


__version__ = str(SemanticVersion('0.1.2'))
