import shutil
import glob
import os
from os import path
from codecs import open
from typing import List, Optional

def flatpack(
    src_folder : str,
    destination_namespace : str, 
    helpers_path_component : str = '_helpers', 
    src_tests_folder : Optional[str] = None
) -> List[str]:
    if any(('/' in arg or '.' in arg) for arg in [src_folder, destination_namespace, helpers_path_component]):
        raise Exception("The symbols '/' and '.' are disallowed by flatpack.")
    
    print("flatpack: start")
    print("flatpack: creating '" + destination_namespace + "'.")
    collected_modules = []
    collected_helper_modules = []
    if path.isdir(destination_namespace):
        shutil.rmtree(destination_namespace)
    os.mkdir(destination_namespace)
    os.mkdir(path.join(destination_namespace, helpers_path_component))
    for srcfilepath in glob.glob(src_folder + '/**/*.py', recursive=True):
        filename = path.basename(srcfilepath)
        if (filename != '__init__.py'):
            module_name = path.splitext(filename)[0]
            is_helper_module = helpers_path_component in srcfilepath
            if is_helper_module:
                collected_helper_modules.append(module_name)
            else:
                collected_modules.append(module_name)
            
            dest_filepath = path.join(destination_namespace, filename) if not is_helper_module else path.join(destination_namespace, helpers_path_component, filename)
            with open(srcfilepath, encoding='utf-8') as src_file:
                lines = src_file.read().splitlines()
                with open(dest_filepath, "x", encoding='utf-8') as destination_file:
                    for line in lines:
                        if (line.startswith('from ' + src_folder)):
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
                if not line.startswith('from ' + src_folder) and ' import ' in line and not ',' in line:
                    raise Exception("Each line in '" + src_folder + "/__init__.py' should start with 'from " + src_folder + "' and should contain a single import, which is not the case for '" + line + "'.")
                init_module = line.split(' ')[-1]
                dest_root_init.write('from .' + init_module + ' import ' + init_module + '\n')
    if len(collected_helper_modules) > 0:
        with open(path.join(destination_namespace, helpers_path_component, '__init__.py'), "x", encoding='utf-8') as dest_helpers_init:
            dest_helpers_init.write('')
    
    if src_tests_folder is None:
        print("flatpack: skip creating tests because 'src_tests_folder' is not provided.")
    else:
        flatpack_tests_folder = 'flatpacked_' + destination_namespace + '_tests'

        print("flatpack: creating '" + flatpack_tests_folder + "'.")

        if path.isdir(flatpack_tests_folder):
            shutil.rmtree(flatpack_tests_folder)
        os.mkdir(flatpack_tests_folder)
        for srctestfilepath in glob.glob(src_tests_folder + '/**/*.*', recursive=True):
            desttestfilepath = os.path.join(flatpack_tests_folder, os.path.relpath(srctestfilepath, (src_tests_folder)))
            filename = path.basename(srctestfilepath)
            directories = desttestfilepath[:-len(filename)]
            if not os.path.exists(directories):
                os.makedirs(directories)
            if srctestfilepath.endswith('.py'):
                with open(srctestfilepath, encoding='utf-8') as srctest_file:
                    lines = srctest_file.read().splitlines()
                    with open(desttestfilepath, "x", encoding='utf-8') as destination_file:
                        for line in lines:
                            if (line.startswith('from ' + src_folder)):
                                if helpers_path_component in line:
                                    modules = [m.strip() for m in line.split(' import ')[-1].split(',')]
                                    for module in modules:
                                        destination_file.write('from ' + destination_namespace + '.' + helpers_path_component + '.' + module + ' import ' + module + '\n')
                                else:
                                    destination_file.write('from ' + destination_namespace + ' import ' + line.split(' import ')[-1] + '\n')
                            else:
                                destination_file.write(line + '\n')
            elif not srctestfilepath.endswith('.pyc'):
                shutil.copyfile(srctestfilepath, desttestfilepath)
    print('flatpack: ready')
    return [destination_namespace] if len(collected_helper_modules) == 0 else [destination_namespace, destination_namespace + '.' + helpers_path_component]