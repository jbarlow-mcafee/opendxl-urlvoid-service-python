from __future__ import absolute_import
import os

from setuptools import setup
import distutils.command.sdist

import setuptools.command.sdist

# Patch setuptools' sdist behaviour with distutils' sdist behaviour
setuptools.command.sdist.sdist.run = distutils.command.sdist.sdist.run

version_info = {}
cwd=os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(cwd, "dxlurlvoidservice", "_version.py")) as f:
    exec(f.read(), version_info)

dist = setup(
    # Package name:
    name="dxlurlvoidservice",

    # Version number:
    version=version_info["__version__"],

    # Requirements
    install_requires=[
        "requests",
        "dxlbootstrap>=0.1.3",
        "dxlclient"
    ],

    # Package author details:
    author="McAfee LLC",

    # License
    license="Apache License 2.0",

    # Keywords
    keywords=['opendxl', 'dxl', 'mcafee', 'service', 'urlvoid', 'urlvapi'],

    # Packages
    packages=[
        "dxlurlvoidservice",
        "dxlurlvoidservice._config",
        "dxlurlvoidservice._config.sample",
        "dxlurlvoidservice._config.app"],

    package_data={
        "dxlurlvoidservice._config.sample" : ['*'],
        "dxlurlvoidservice._config.app" : ['*']},

    # Details
    url="http://www.mcafee.com/",

    description="URLVoid API DXL service library",

    long_description=open('README').read(),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
)
