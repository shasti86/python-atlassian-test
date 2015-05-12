from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='msgservice',
    version='1.0.0',
    description='Atlassian Test Application',
    author='Shastinathan Sivasubramanian',
    author_email='shastinathan.s@gmail.com',
    test_suite='',
    install_requires=required,
    url=''
)
