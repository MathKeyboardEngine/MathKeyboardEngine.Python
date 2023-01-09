import shutil
import glob
import os
from os import path
from codecs import open
from typing import List

def flatpack(src_folder : str, destination_namespace : str, helpers_path_component : str = '_helpers') -> List[str]:
    if any(('/' in arg or '.' in arg) for arg in [src_folder, destination_namespace, helpers_path_component]):
        raise Exception("The symbols '/' and '.' are disallowed by flatpack.")

    collected_modules = []
    collected_helper_modules = []
    if path.isdir(destination_namespace):
        shutil.rmtree(destination_namespace)
    os.mkdir(destination_namespace)
    os.mkdir(path.join(destination_namespace, helpers_path_component))
    for filepath in glob.glob(src_folder + '/**/*.py', recursive=True):
        filename = path.basename(filepath)
        if (filename != '__init__.py'):
            module_name = path.splitext(filename)[0]
            is_helper_module = helpers_path_component in filepath
            if is_helper_module:
                collected_helper_modules.append(module_name)
            else:
                collected_modules.append(module_name)
            with open(filepath, encoding='utf-8') as src_file:
                dest_filepath = path.join(destination_namespace, filename) if not is_helper_module else path.join(destination_namespace, helpers_path_component, filename)
                print(dest_filepath)
                with open(dest_filepath, "x", encoding='utf-8') as destination_file:
                    lines = src_file.read().splitlines()
                    for line in lines:
                        if (line.startswith('from src')):
                            modules = [m.strip() for m in line.split(' import ')[-1].split(',')]
                            for module in modules:
                                destination_file.write('from ' + (destination_namespace + '.' + helpers_path_component if helpers_path_component in line else destination_namespace) + '.' + module + ' import ' + module + '\n')
                        else:
                            destination_file.write(line + '\n')

    with open(path.join(destination_namespace, '__init__.py'), 'x') as dest_root_init:
        with open(path.join(src_folder, '__init__.py'), 'r') as src_root_init:
            lines = src_root_init.read().strip().splitlines()
            for line in lines:
                if helpers_path_component in line:
                    raise Exception("The __init__.py from '" + src_folder + "' should not contain '" + helpers_path_component + "'.")
                init_module = line.split(' ')[-1]
                dest_root_init.write('from .' + init_module + ' import ' + init_module + '\n')
    if len(collected_helper_modules) > 0:
        with open(path.join(destination_namespace, helpers_path_component, '__init__.py'), "x", encoding='utf-8') as dest_helpers_init:
            dest_helpers_init.write('')
    return [destination_namespace] if len(collected_helper_modules) == 0 else [destination_namespace, destination_namespace + '.' + helpers_path_component]
