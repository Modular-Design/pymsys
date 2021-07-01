from setuptools import setup

setup(
    name="pymsys",
    install_requires=[
        "setuptools~=56.0",
        "fastapi~=0.65",
        "uvicorn~=0.13",
        "click~=7.0",
    ],
    extra_require={
        "pytest~=6.2.3",
    },
)
