import shutil
from codecs import open
from os import path
import glob
import os

def flatpack(src_folder :str, destination_folder : str):
    collected_modules = []
    if os.path.isdir(destination_folder):
        shutil.rmtree(destination_folder)
    os.mkdir(destination_folder)
    for file in glob.glob(src_folder.strip('/') + '/**/*.py', recursive=True):
        filename = os.path.basename(file)
        if (filename != '__init__.py'):
            with open(file, encoding='utf-8') as src_file:
                collected_modules.append(os.path.splitext(filename)[0])
                with open(path.join(destination_folder, filename), "x", encoding='utf-8') as destination_file:
                    lines = src_file.read().splitlines()
                    for line in lines:
                        if (line.startswith('from src')):
                            modules = [m.strip() for m in line.split(' import ')[-1].split(',')]
                            for module in modules:
                                destination_file.write('from .' + module + ' import ' + module + '\n')
                        else:
                            destination_file.write(line + '\n')

    with open(path.join(destination_folder, '__init__.py'), 'x') as destination_init:
        destination_init.writelines([('from .' + m + ' import ' + m + '\n') for m in collected_modules])