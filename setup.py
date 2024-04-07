from setuptools import find_packages, setup
from typing import List

HYEN_E_DOT='-e .'
def get_requirements(file_path: str) -> list:
    """Read a file and return its content as a list of strings."""
             
    requirements=[]
    with open(file_path)as file_obj:
            requirements=file_obj.readlines()
    requirements=[req.replace("\n","")for req in requirements]
    if HYEN_E_DOT in requirements:
        requirements.remove(HYEN_E_DOT)
    return requirements


setup(
    name='ML Project',
    version='0.0.1',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    # Metadata
    author='Rahul Kumar',
    author_email='rk3342377@gmail.com',
    description='''Project utilizes deep learning techniques to classify images of handwritten digits with high accuracy.
                 The model, trained on the MNIST dataset, achieves state-of-the-art performance in digit recognition tasks.''',
    url='https://github.com/rahul0607830/ML-Projects',
)
