from setuptools import find_packages, setup

setup(
    name='tsundere',
    author='Paul Traylor',
    url='http://github.com/kfdm/tsundere/',
    packages=find_packages(exclude=['test']),
    install_requires=[
        'Django == 1.8.2',
    ],
    entry_points={
        'django.apps': [
            'pluggable = pluggable',
        ],
    }
)
