# Setup.py file to facilitate distribution of software.

from setuptools import setup
setup(
    name='MeshMapper',
    version='0.1dev',
    packages=['.'],
    install_requires=[
            'sys',
            'math',
            'requests',
            'matplotlib',
            'tkinter',
            'PIL',
            'osmnx',
            'networkx',
        ]
    #liscense='',
    #long_description=open('README.txt').read()
)
