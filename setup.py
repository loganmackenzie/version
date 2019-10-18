"""`version` lives on `GitHub <http://github.com/loganmackenzie/version/>`_."""
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

from semantic_version import __version__


setup(
    name='version',
    version=__version__,
    author='Vladimir Keleshev',
    author_email='vladimir@keleshev.com',
    maintainer='Logan MacKenzie',
    maintainer_email='loganmackenzie1@gmail.com',
    description='Versioning system with semantic versioning and generic version formats',
    license='MIT',
    keywords='semver semantic version versioning versions',
    url='http://github.com/loganmackenzie/version',
    py_modules=['nonsemantic_version', 'semantic_version'],
    long_description=long_description,
    long_description_content_type='text/markdown'
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ]
)
