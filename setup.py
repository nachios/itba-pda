from setuptools import setup

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name='pda',
    version='0.0.1',
    author='Tato',
    author_email='nacho.santangelo@gmail.com',
    install_requires=install_requires,
    packages=['pda']
)
