from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='cheesebox',
    version='0.0.2',
    packages=find_packages(),
    license="MIT",
    description='A REPL that (somewhat) understands mathematical expressions written in natural language.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='dejmedus',
    author_email='hi@juliab.dev',
    url='https://github.com/dejmedus/cheesebox',
    entry_points={
        "console_scripts": [
            "cheesebox = cheesebox.main:main",
        ],
    },
)