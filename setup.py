
from distutils.core import setup
from setuptools import find_packages


with open('requirements.txt') as f:
    requirements = f.readlines()


setup(
    name = 'TimeToolBox',
    version = 'v0.1.0',
    author = 'Jessy Khafif',
    author_email = 'khafifjessy.github@gmail.com',
    packages = find_packages(),
    license = 'MIT',
    install_requires=requirements
)