from setuptools import setup

# To use a consistent encoding
from codecs import open
from os import path

root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mathkeyboardengine",
    version="0.1.0-alpha",
    description="MathKeyboardEngine provides the logic for a highly customizable virtual math keyboard. It is intended for use together with any LaTeX typesetting library.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python",
    author="MathKeyboardEngine",
    author_email="symbolinker@gmail.com",
    license="ISC",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["src"]
)