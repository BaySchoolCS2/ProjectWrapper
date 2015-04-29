from setuptools import setup

setup(
    name = 'PWrapper',
    py_modules = ['pwrapper'],
    version = '0.0.8',
    description = 'api wrapper',
    author = 'Finley Hebert-Perkins',
    url = 'https://github.com/BaySchoolCS2/ProjectWrapper',
    install_requires=[
        'requests>=1.1.0'
    ]
)
