#!/usr/bin/env python

from setuptools import setup, find_packages

with open("README.rst") as f:
	long_description = f.read()

setup(name="listdiff",
	version="0.2",
	description="Diff lists",
	long_description=long_description,
	author="Rehan Khwaja",
	author_email="rehan@khwaja.name",
	url="https://github.com/rkhwaja/pylistdiff",
	packages=find_packages(),
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7"
	],
	keywords="",
)