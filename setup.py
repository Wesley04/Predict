from setuptools import setup, find_packages

setup(
    name='predict',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA predict python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Wesley04/predictpackage',
    author='Wesley04',
    author_email='wesnagiah@gmail.com'
)
