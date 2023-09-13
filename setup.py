from setuptools import setup, find_packages

# This is used in Jenkins to assign version in artifactory.
__version__ = '0.3.22'

setup(
    name='etl',
    version=__version__,
    description='etl as code',
    author='none',
    author_email='rama@rama.com',
    long_description=long_description,
    url='https://github.com/ramadhanptrr/pythoncicd/tree/main/datamart_module',
    packages=find_packages(where='datamart_module'),
    package_dir={"": "datamart_module"}
)
