from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

# Method that reads requirements.txt and returns the list 
# of required packages. Since there is a new line after every package
# we need to replace new line with blank. 
# Also in requirements.txt we are using '-e .' which tells the requirement.txt
# to invoke setup.py and hence we need to remove that while preparing packages.
def get_requirements(file_path:str)->List[str]:
    '''
        this function will return the list of requirements.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# This method will be invoked when install command is run.
# Installs the required packages for the python program.
setup(
    name='mlproject',
    version='0.0.1',
    author='Mahesh',
    author_email='maahi333@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirement.txt')
)