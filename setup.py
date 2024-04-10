from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cheesebox',
    version='0.1',
    packages=find_packages(),
    description='semantic calculations',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='dejmedus',
    author_email='hi@juliab.dev',
    url='https://github.com/dejmedus/cheesebox',
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "cheesebox = main:main",
        ],
    },
)