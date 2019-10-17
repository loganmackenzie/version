from pytest import raises

from base_version import VersionError
from nonsemantic_version import NonSemanticVersion

'''
def test_nonsemantic_versions():
    """Test revisions

    Test handling nonsemantic versions. Ensure that regenerating the version
    strings works correctly. Ensure that parsing the version strings is
    correct. And that the version comparisons are correct.
    """
    assert str(NonSemanticVersion('0')) == '0'
    assert repr(NonSemanticVersion('0')) == "NonSemanticVersion('0')"
    assert repr(NonSemanticVersion('0-alpha')) == "NonSemanticVersion('0-alpha')"
    assert repr(NonSemanticVersion('0-alpha+12321')) == "NonSemanticVersion('0-alpha+12321')"
    assert str(NonSemanticVersion('1.2')) == '1.2'
    assert repr(NonSemanticVersion('1.2')) == "NonSemanticVersion('1.2')"
    assert repr(NonSemanticVersion('1.2-beta.1')) == "NonSemanticVersion('1.2-beta.1')"
    assert repr(NonSemanticVersion('1.2-beta.1+4432.332')) == "NonSemanticVersion('1.2-beta.1+4432.332')"
    assert str(NonSemanticVersion('0.0.0')) == '0.0.0'
    assert repr(NonSemanticVersion('0.0.0')) == "NonSemanticVersion('0.0.0')"
    assert str(NonSemanticVersion('999.999.999.999')) == '999.999.999.999'
    assert repr(NonSemanticVersion('999.999.999.999')) == "NonSemanticVersion('999.999.999.999')"
    assert str(NonSemanticVersion('999.abc.999.999')) == '999.abc.999.999'
    assert repr(NonSemanticVersion('999.abc.999.999')) == "NonSemanticVersion('999.abc.999.999f')"
    assert str(NonSemanticVersion('999.abc.999.999f')) == '999.abc.999.999'
    assert repr(NonSemanticVersion('999.abc.999.999f')) == "NonSemanticVersion('999.abc.999.999f')"

    with raises(VersionError):
        NonSemanticVersion('X.Y.Z')

    assert NonSemanticVersion('1.2.3.4')._revisions() == [(1, ''), (2, ''), (3, ''), (4, '')]
    assert NonSemanticVersion('1a.2b.3c.4d')._revisions() == [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
    assert NonSemanticVersion('1.2.3.f')._revisions() == [(1, ''), (2, ''), (3, ''), (None, '')]

    assert NonSemanticVersion('1.9.0') < NonSemanticVersion('1.10.0') < NonSemanticVersion('1.11.0')
    assert NonSemanticVersion('1.9.0.3') < NonSemanticVersion('1.10.0.1') < NonSemanticVersion('1.11.0.f')
    assert NonSemanticVersion('1.9.0.3') < NonSemanticVersion('1.10.0.1') < NonSemanticVersion('1.11.0.f')
    assert NonSemanticVersion('2.9.0') < NonSemanticVersion('1.10.0.0') < NonSemanticVersion('a.0.0.3')
    assert NonSemanticVersion('1.9.0.3') < NonSemanticVersion('1.9.0.4') < NonSemanticVersion('1.9.0.f')
    assert NonSemanticVersion('13') < NonSemanticVersion('1.0') < NonSemanticVersion('1.0.1')



def test_section_10():
    """Semantic Version Section 10: Pre-release version.

    A pre-release version MAY be denoted by appending a dash
    and a series of dot separated identifiers immediately
    following the patch version. Identifiers MUST be
    comprised of only ASCII alphanumerics and dash
    [0-9A-Za-z-]. Pre-release versions satisfy but have a
    lower precedence than the associated normal version.
    Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7,
    1.0.0-x.7.z.92.

    """
    assert NonSemanticVersion('1.0.0').pre_release == []
    assert NonSemanticVersion('1.0.0-alpha').pre_release == ['alpha']
    assert NonSemanticVersion('1.0.0-alpha.1').pre_release == ['alpha', 1]
    assert NonSemanticVersion('1.0.0-0.3.7').pre_release == [0, 3, 7]
    assert NonSemanticVersion('1.0.0-x.7.z.92').pre_release == ['x', 7, 'z', 92]
    assert str(NonSemanticVersion('1.0.0-x.7.z.92')) == '1.0.0-x.7.z.92'
    assert NonSemanticVersion('1.0.0.0').pre_release == []
    assert NonSemanticVersion('1.0.0.0-alpha').pre_release == ['alpha']
    assert NonSemanticVersion('1.0.0.0-alpha.1').pre_release == ['alpha', 1]

    with raises(VersionError):
        NonSemanticVersion('1.0.0-')
    with raises(VersionError):
        NonSemanticVersion('1.0.0-$#%')

    assert NonSemanticVersion('1.0.0') > NonSemanticVersion('1.0.0-alpha')
    assert NonSemanticVersion('1.0.0-alpha') < NonSemanticVersion('1.0.0')


def test_section_11():
    """Semantic Version Section 11: Build version.

    A build version MAY be denoted by appending a plus sign
    and a series of dot separated identifiers immediately
    following the patch version or pre-release version.
    Identifiers MUST be comprised of only ASCII
    alphanumerics and dash [0-9A-Za-z-]. Build versions
    satisfy and have a higher precedence than the associated
    normal version. Examples: 1.0.0+build.1,
    1.3.7+build.11.e0f985a.

    """
    assert NonSemanticVersion('1.0.0+build.1').build == ['build', 1]
    assert NonSemanticVersion('1.0.0+build.11.e0f985a').build == ['build', 11, 'e0f985a']
    assert NonSemanticVersion('1.0.0.f+build.1').build == ['build', 1]
    assert NonSemanticVersion('1.0.0.f+build.11.e0f985a').build == ['build', 11, 'e0f985a']


def test_section_12():
    """Section 12: Precedence rules.

    Precedence MUST be calculated by separating the version
    into major, minor, patch, pre-release, and build
    identifiers in that order. Major, minor, and patch
    versions are always compared numerically. Pre-release
    and build version precedence MUST be determined by
    comparing each dot separated identifier as follows:
    identifiers consisting of only digits are compared
    numerically and identifiers with letters or dashes are
    compared lexically in ASCII sort order. Numeric
    identifiers always have lower precedence than
    non-numeric identifiers. Example: 1.0.0-alpha <
    1.0.0-alpha.1 < 1.0.0-beta.2 < 1.0.0-beta.11 <
    1.0.0-rc.1 < 1.0.0-rc.1+build.1 < 1.0.0 < 1.0.0+0.3.7 <
    1.3.7+build < 1.3.7+build.2.b8f12d7 <
    1.3.7+build.11.e0f985a.

    """
    presorted = [
        '1.0.0.0-alpha',
        '1.0.0.0-alpha.1',
        '1.0.0.0-beta.2',
        '1.0.0.0-beta.11',
        '1.0.0.0-rc.1',
        '1.0.0.0-rc.1+build.1',
        '1.0.0.0',
        '1.0.0.0+0.3.7',
        '1.3.7.0+build',
        '1.3.7.0+build.2.b8f12d7',
        '1.3.7.0+build.11.e0f985a',
    ]
    from random import shuffle
    randomized = list(presorted)
    shuffle(randomized)
    fixed = list(map(str, sorted(map(NonSemanticVersion, randomized))))
    assert fixed == presorted


def test_comparing_against_non_version():

    with raises(TypeError) as exception:
        NonSemanticVersion('1.0.0') > None
    assert 'cannot compare' in repr(exception.value)

    with raises(TypeError) as exception:
        NonSemanticVersion('1.0.0') == object()
    assert 'cannot compare' in repr(exception.value)
'''
