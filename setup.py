from setuptools import setup, find_packages

setup(
    name="calculator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "calculator=calculator.__main__:main",
        ],
    },
    author="skittally",
    description="A simple calculator application with theme support",
)
