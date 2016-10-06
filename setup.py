# -*- coding: utf-8 -*-
"""Pseudorandom ID generation with fun, unique animal ID's."""
from setuptools import setup


LONG_DESCRIPTION = """
animalid is a simple library for generating fun, unique animal ID's.

ID's are strings composed of lowercase ascii letters and underscores, with a
number of adjectives followed by an animal name.

Use this library to generate unique ID's that are memorable and easy to read
and type.
"""

test_requirements = [
    'pydocstyle',
    'pytest',
    'pytest-flake8',
    'pytest-pep8',
    'pytest-mccabe',
    'pytest-cov',
]

release_requirements = [
    'twine',
    'zest.releaser']

setup(name='animalid',
      version='0.0.3.dev0',
      description=('Library and CLI tool for generating '
                   'unique IDs with animal names.'),
      author='Alex Conway',
      author_email='alex@datarobot.com',
      url='https://github.com/datarobot/animalid',
      license='Freely Distributable',
      long_description=LONG_DESCRIPTION,
      packages=['animalid'],
      zip_safe=False,
      extras_require={
          'dev': release_requirements + test_requirements,
          'release': release_requirements,
          'testing': test_requirements},
      tests_require=test_requirements,
      test_suite='tests',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Topic :: Utilities',
          'License :: Freely Distributable',
          'Programming Language :: Python :: 2.7'],
      keywords=['random', 'id', 'unique', 'identifier'])
