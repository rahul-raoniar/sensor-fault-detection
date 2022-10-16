from setuptools import find_packages, setup


def get_requirements():
    '''This return a requirement list'''
    requirement_list = []

    """
    # Assignment 1: write code to read requirement.txt file
    and add them to requirement variable
    """
    return requirement_list

setup(
    name = "sensor",
    version = "0.0.1",
    author = "Rahul Raoniar",
    author_email = "rahul.raoniar@outlook.com",
    packages = find_packages(),
    install_requires = get_requirements() #[]
)