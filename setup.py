from setuptools import setup,find_packages
with open('requirements.txt') as f:
    requirements=f.read().splitlines()
    
setup(
    name="Movie Recommender",
    version='0.1',
    author="Mani",
    packages=find_packages(),
    install_requires=requirements
)