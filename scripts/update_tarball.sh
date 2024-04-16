#!/bin/bash

version=$(python setup.py --version)

python setup.py sdist bdist_wheel

sha256=$(shasum -a 256 dist/cheesebox-$version.tar.gz | cut -d ' ' -f 1)

pip install dist/cheesebox-$version-py3-none-any.whl --force-reinstall

sed -i '' "s|url \".*\"|url \"https://github.com/dejmedus/cheesebox/cheesebox-$version.tar.gz\"|" ./cheesebox.rb
sed -i '' "s|sha256 \".*\"|sha256 \"$sha256\"|" ./cheesebox.rb