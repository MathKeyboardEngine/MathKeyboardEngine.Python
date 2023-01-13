import shutil
from setuptools import setup
from codecs import open
import os
from os import path
from _disthelper.flatpack import flatpack

for dir in ['dist', 'mathkeyboardengine.egg-info', 'build']:
    if os.path.isdir(dir):
        shutil.rmtree(dir)

root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mathkeyboardengine",
    version="0.1.0-alpha.24",
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
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent"
    ],
    packages=flatpack(src_folder='src', destination_namespace='mathkeyboardengine')
)