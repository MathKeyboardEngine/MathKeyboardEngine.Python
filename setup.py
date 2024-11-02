import os
import shutil
from codecs import open
from os import path

from setuptools import setup

from _disthelper.flatpack import flatpack

for dir in ['dist', 'mathkeyboardengine.egg-info', 'build']:
    if os.path.isdir(dir):
        shutil.rmtree(dir)

root_dir = path.abspath(path.dirname(__file__))
with open(path.join(root_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mathkeyboardengine',
    version='1.0.0-beta',
    description='MathKeyboardEngine provides the logic for a highly customizable virtual math keyboard. It is intended for use together with any LaTeX typesetting library.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python',
    author='MathKeyboardEngine',
    author_email='symbolinker@gmail.com',
    license='0BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Operating System :: OS Independent',
    ],
    packages=flatpack(src_folder='src', destination_namespace='mathkeyboardengine'),
)
