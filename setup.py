"""
setup tools
"""
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
    ],
)

# MANIFEST.in: This tells Python to copy everything in the static and templates
#  directories, and the schema.sql file, but to exclude all bytecode files.
