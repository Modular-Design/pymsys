from setuptools import setup
import os
import sys
import warnings


def local_file(name):
    return os.path.relpath(os.path.join(os.path.dirname(__file__), name))


SOURCE = local_file("src")
README = local_file("README.md")

extras = {"test": ["pytest>=6.2.3", "requests>=2.26.0"]}

setup(
    name="pymsys",
    description="MSYS Library for Python.",
    install_requires=[
        "setuptools~=56.0",
        "fastapi~=0.65",
        "uvicorn~=0.13",
        "click~=7.0",
    ],
    extras_require=extras,
    long_description=open(README).read(),
    long_description_content_type="text/markdown",
)
