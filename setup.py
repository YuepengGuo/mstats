# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='mstats',
    version = '1.0.0',
    description= 'show the basic statis of the market',
    author = 'william',
    author_email = 'xx@gmail.com',
    url = 'https://github.com/YuepengGuo',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'stats = mstats.mstats:main',
        ]
    },
    install_requires=[
        'requests',
    ]
)
