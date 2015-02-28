from distutils.core import setup
from setuptools import find_packages

setup(
    name='pandas-highcharts',
    version='0.3.0',
    author='Guillaume Thomas',
    author_email='guillaume.thomas642@gmail.com',
    license='LICENSE',
    description='pandas-highcharts is a Python package which allows you to easily build Highcharts plots with pandas.DataFrame objects.',
    url='https://github.com/gtnx/pandas-highcharts',
    install_requires=map(
        lambda line: line.strip("\n"),
        open("requirements.txt", "r").readlines()
    ),
    include_package_data=True,
    packages=find_packages(),
)
