from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(filename:str)->List[str]:
    """
    This function returns list of requirements from a filepath
    """
    requirements = [line.strip() for line in open(filename).readlines()]
    
    if HYPHEN_E_DOT in requirements:
        requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name = 'Language-detection-app',
    version = '0.1',
    author = 'Ameer',
    packages = find_packages(),
    install_requires = get_requirements('requirements.txt')
)