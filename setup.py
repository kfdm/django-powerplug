from setuptools import setup

setup(
    name='tsundere',
    author='Paul Traylor',
    url='http://github.com/kfdm/tsundere/',
    packages=['tsundere'],
    install_requires=[
        'Django == 1.8.2',
        'python-social-auth',
    ],
    entry_points={
        'console_scripts': [
            'tsundere = tsundere.manage:main'
        ]
    }
)
