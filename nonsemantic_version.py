"""Non-semantic versioning"""
import sys
import re

if sys.version_info >= (3, 0):
    from itertools import zip_longest as izip_longest
else:
    from itertools import izip_longest
from base_version import BaseVersion, VersionError, _Seq


class NonSemanticVersion(BaseVersion):
    """ Support non-semantic versions """
    # Note: positive lookahead to handle an empty string.
    REV_REGEX = re.compile('^(?=.*.)(\d*)([A-Za-z]*)$')

    def __init__(self, version):
        self.revisions = []
        self.pre_release = None
        self.build = None
        try:
            self._parse_version(version)
        except ValueError:
            raise VersionError('Invalid version %r. Multiple pre-release or build versions.', version)
        except AttributeError:
            raise VersionError('Invalid version %r. Invalid revision.', version)
        except Exception:
            raise VersionError('Invalid version %r', version)

    def _revisions(self):
        return self.revisions

    def _parse_rev(self, rev):
        """Parse a revision"""
        int_val, str_val = self.REV_REGEX.match(rev).groups()
        return (int(int_val) if int_val else None, str_val)

    def _parse_version(self, version):
        """Parse the version"""
        self.revisions = []
        # Split at '.' until we reach either '-' or '+'
        # Build ('+') should always come after pre-release ('-')
        # Step 1: Try to split on '+' and pull the build version off.
        if self.BUILD_DELIMITER in version:
            version, build = version.split(self.BUILD_DELIMITER)
            self.build = self._make_group(build)
        # Step 2: Try to split on '-' nad pull the pre-release version off.
        if self.PRE_RELEASE_DELIMITER in version:
            version, pre_release = version.split(self.PRE_RELEASE_DELIMITER)
            self.pre_release = self._make_group(pre_release)
        # Step 3: Split on '.' and parse revisions until we run out.
        while self.REVISION_DELIMITER in version:
            rev, version = version.split(self.REVISION_DELIMITER, 1)
            self.revisions.append(self._parse_rev(rev))
        # Parse the last revision
        self.revisions.append(self._parse_rev(version))

    def __lt__(self, other):
        try:
            return super().__lt__(other)
        except TypeError as err:
            # TypeError in comparing revisions
            for s, o in izip_longest(self._revisions(), other._revisions()):
                if s is None or o is None:
                    return bool(s is None)
                if type(s[0]) is not type(o[0]):
                    return type(s[0]) is int
                elif type(s[1]) is not type(o[1]):
                    return type(s[1]) is int

    @staticmethod
    def _str_rev(rev):
        return ''.join(['' if s is None else str(s) for s in rev])





def test_parsing_and_stringification():
    revisions = ['1', '1f', '1.2', '1.f', '1e.f', '1.2.0', '1.2.0f', '1.2e.0f', '1.2.0.1f', '1.2.0f.1f', '1.2.0f.1', '1.2e.0f.1f', '1.2.0.1.4f']
    for rev in revisions:
        non = NonSemanticVersion(rev)
        print(f'{rev:<12} --> {str(non):<12} == {rev == str(non)}')

if __name__ == '__main__':
    test_parsing_and_stringification()
    # print(NonSemanticVersion.parse('1.2.0f.1f'))
