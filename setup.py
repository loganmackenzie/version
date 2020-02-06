"""`enhanced-versioning` lives on `GitHub <http://github.com/loganmackenzie/enhanced-versioning>`_."""
from setuptools import find_packages, setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

from enhanced_versioning import __version__


setup(
    name='enhanced-versioning',
    version=__version__,
    author='Logan MacKenzie',
    author_email='loganmackenzie1@gmail.com',
    maintainer='Logan MacKenzie',
    maintainer_email='loganmackenzie1@gmail.com',
    description='Versioning system with semantic versioning and generic version formats',
    license='MIT',
    keywords='semver semantic version versioning versions',
    url='http://github.com/loganmackenzie/enhanced-versioning',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Utilities'
    ]
)
