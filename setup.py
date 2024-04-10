from setuptools import setup, find_packages

setup(
    name='cheesebox',
    version='0.1',
    packages=find_packages(),
    description='semantic calculations',
    author='dejmedus',
    author_email='hi@juliab.dev',
    url='https://github.com/dejmedus/cheesebox',
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "cheesebox = cheesebox.main:main",
        ],
    },
)