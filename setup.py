import shutil
from setuptools import setup
from codecs import open
from os import path
import glob
import os
collected_modules = []
temp_dist = 'mathkeyboardengine'
if os.path.isdir(temp_dist):
    shutil.rmtree(temp_dist)
os.mkdir(temp_dist)
for file in glob.glob('src/**/*.py', recursive=True):
    with open(file, encoding='utf-8') as srcFile:
        fileName = os.path.basename(file)
        collected_modules.append(fileName.split('.')[0])
        with open(path.join(temp_dist, fileName), "x", encoding='utf-8') as distFile:
            lines = srcFile.read().splitlines()
            for line in lines:
                if (line.startswith('from src')):
                    modules = line.split(' import ')[-1].split(', ')
                    for module in modules:
                        distFile.write('from .' + module + ' import ' + module + '\n')
                else:
                    distFile.write(line + '\n')

with open(path.join(temp_dist, '__init__.py'), 'w') as init:
    init.writelines([('from .' + m + ' import ' + m + '\n') for m in collected_modules])

root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="mathkeyboardengine",
    version="0.1.0-alpha.11",
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
    packages=["mathkeyboardengine"]
)