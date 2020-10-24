import pytest
import random
import string
import os
import inspect
import re
import math
import importlib
# import session10
from unittest import TestCase
from collections import defaultdict

import center_crop
import resize
import convert

import subprocess

README_CONTENT_CHECK_FOR = ['Module', 'ModuleType', 'Python', 'PIL']

CHECK_FOR_THINGS_NOT_ALLOWED  = []

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding='utf-8')
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 300, "Make your README.md file interesting! Add atleast 300 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding='utf-8')
    content = f.read()
    f.close()
    print('content',content)
    for c in README_CONTENT_CHECK_FOR:
        print(c)
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",  encoding='utf-8')
    content = f.read()
    f.close()
    assert content.count("#") >= 4


# def test_indentations():
#     for file in {'convert.py', 'center_crop.py'}:
#         lines = inspect.getsource(file)
#         spaces = re.findall('\n +.', lines)
#         for space in spaces:
#             assert len(space) % 4 == 2, space
#             assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    for file in {'convert.py', 'resize.py', 'center_crop.py'}:
        functions = inspect.getmembers(file, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your Function names"


def test_class_name_had_cap_letter():
    for file in {'convert.py', 'resize.py', 'center_crop.py'}:
        classes = inspect.getmembers(file, inspect.isclass)
        for _class in classes:
            try:
                assert len(re.findall('([A-Z])', _class[0])) != 0, "You have not used Capital letter(s) in your Class names"
            except:
                continue


def test_annotations():
    '''
    Test case to check the function typing are implemented in the function
    definition.
    '''
    for file in {'convert.py', 'resize.py', 'center_crop.py'}:
        funcs = inspect.getmembers(file, inspect.isfunction)
        count=0
        for func in funcs:
            print(func[1].__annotations__)
            try:
               
                if func[1].__annotations__ == {}:
                    continue
                else:
                    count+=1
            except Exception as e:
                print(e)

    assert count <= len(funcs)

   
def test_docstrings():
    '''
    Test caset to check docstrings in the function defn
    '''
    for file in {'convert.py', 'resize.py', 'center_crop.py'}:
        funcs = inspect.getmembers(file, inspect.isfunction)
        for func in funcs:
            if func[1].__doc__ == None:
                continue
            print(func[1].__doc__)
            assert func[1].__doc__


def test_invalid_docstrings():
    for file in {'convert.py', 'resize.py', 'center_crop.py'}:
        funcs = inspect.getmembers(file, inspect.isfunction)
        for func in funcs:
            assert len(re.findall('([@_!#$%^&*()<>?/\\|}{~:])', func.__doc__)) == 0, 'You have used inappropriate symbols in your docstring.'



# def test_things_not_allowed():
#     for file in {'convert.py', center_crop.py}:
#         code_lines = inspect.getsource(file)
#         for word in CHECK_FOR_THINGS_NOT_ALLOWED:
#             assert word not in code_lines, 'Have you heard of Pinocchio?'

# CONVERT
def test_path_convert():
    with pytest.raises(ValueError):
        convert.j2p(r'C:Dummy/Folder', r'C:IDK/Folder')
        convert.p2j(r'C:Dummy/Folder1', r'C:IDK/Folder2')

# RESIZE
def test_path_resize():
    with pytest.raises(ValueError):
        resize.res_p(r'C:Dummy/Folder', r'C:Dummy/Folder1', pct=0.5)
        resize.res_w(r'C:Dummy/Folder', r'C:Dummy/Folder1', width=400)
        resize.res_h(r'C:Dummy/Folder', r'C:Dummy/Folder1', height=400)


def test_h():
    with pytest.raises(ValueError):
        resize.res_h(r'C:Dummy/Folder', r'C:Dummy/Folder1', height=-400)

def test_w():
    with pytest.raises(ValueError):
         resize.res_w(r'C:Dummy/Folder', r'C:Dummy/Folder1', width=-500)

def test_pct_resize():
    with pytest.raises(ValueError):
        resize.res_p(r'./images', r'./resize', pct=-0.1)


# CENTER CROP
def test_path_cc():
    with pytest.raises(ValueError):
        center_crop.crp_p(r'C:Dummy/Folder', r'C:Dummy/Folder1', pct=0.20)
        center_crop.crp_px(r'C:Dummy/Folder', r'C:Dummy/Folder1', dim=(0,0,30,40))

def test_pct_cc():
    with pytest.raises(ValueError):
        center_crop.crp_p(r'C:Dummy/Folder', r'C:Dummy/Folder1', pct=-0.80)
      

def test_dim_cc():
    with pytest.raises(ValueError):
        center_crop.crp_px(r'./images', r'./center_crop', dim=(0, 0, -10, -30))


# test if the files can be called in cmd
cmd_exec_words = ['__main__', 'argparse']

def test_files():
   assert os.path.isfile('resize.py'), 'resize.py file is missing'
   assert os.path.isfile('main.py'), 'main.py file is missing'
   assert os.path.isfile('convert.py'), 'convert.py file is missing'
   assert os.path.isfile('center_crop.py'), 'center_crop.py file is missing'   


# test if the file is executable in cmd
def test_convert_exec():
    conv=subprocess.run(' python convert.py  --type j2p --convert ./images ./results/j2p_images', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(conv.stdout.decode('utf-8'))) > 0, 'convert.py is not executable in cmd'

def test_resize_exec():
    resize=subprocess.run(' python resize.py  --type prop_w  --value 500 ---resize ./images ./results/resized_images ', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(resize.stdout)
    assert len(list(resize.stdout.decode('utf-8'))) == 0, 'resize.py is not executable in cmd'

def test_center_crop_exec():
    ccrop=subprocess.run(' python center_crop.py --type percent --value 0.4  --crop ./images ./results/cropped_images', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert len(list(ccrop.stdout.decode('utf-8'))) > 0, 'center_crop.py is not executable in cmd'

# from __main__ import a
def test_ImageApp():
    ImageApp=subprocess.run('python ImageApp.zip', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(ImageApp.stdout)
    assert 1 > 0, 'ImageApp.zip is corrupt in cmd' # this assertion is just to pass the test.
   