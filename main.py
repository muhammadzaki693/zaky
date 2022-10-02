"""
This template is the framework for creating and distributing
packages on the official Python Package Index (or PyPi).

The following os.system commands will help you compile your 
project into a "dist" file for distribution.

Created by @IreTheKID
"""

import os

os.system("rm -r dist")
os.system("rm -r zaki.egg-info")
os.system("rm -r build")
os.system('pip install --upgrade pip')
os.system('pip install wheel')
os.system('pip install twine')
os.system('python zaki_project/setup.py sdist bdist_wheel')
os.system('twine upload dist/*')