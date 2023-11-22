from setuptools import setup, find_packages
import os

# Load requirements from requirements.txt, if it exists
try:
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
except FileNotFoundError:
    requirements = []

setup(
    name='infra-app',
    version='0.1.0',
    description='Infrastructure management application',
    packages=['infra_app'],
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'infra-app = infra_app.app:main',
        ],
    },
)
