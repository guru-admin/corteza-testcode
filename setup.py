# setup.py

from setuptools import setup, find_packages

setup(
    name='my_api_package',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests'
    ]
)