from setuptools import find_packages
from setuptools import setup

setup(
    name='mower_description',
    version='0.0.0',
    packages=find_packages(
        include=('mower_description', 'mower_description.*')),
)
