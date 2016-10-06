# -*- coding: utf-8 -*-
"""Deploy tooling for DataRobot."""


from setuptools import setup


test_requirements = [
    'pydocstyle',
    'pytest',
    'pytest-flake8',
    'pytest-pep8',
    'pytest-mccabe',
    'pytest-cov',
]

release_requirements = [
    # zest releaser fails with twine 1.7
    'twine',
    'zest.releaser']

entry_points = {
    'console_scripts': []}

setup(name='animalid',
      version='0.0.2',
      description=('Library and CLI tool for generating '
                   'unique IDs with animal names.'),
      author='Release Squad',
      author_email='release@datarobot.com',
      entry_points=entry_points,
      url='https://github.com/datarobot/animalid',
      packages=['animalid'],
      extras_require={
          'dev': release_requirements + test_requirements,
          'release': release_requirements,
          'testing': test_requirements},
      tests_require=test_requirements,
      test_suite='tests')
