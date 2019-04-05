from setuptools import setup, find_packages
from rosetta_grappelli import __version__

setup(
    name="django-rosetta-grappelli2",
    version=__version__,
    description="""
    Compatibility templates for django rosetta when using django-grappelli. Continued
    development from the original but stalled django-rosetta-grappelli project.
    """,
    author='Paessler AG',
    author_email="bis@paessler.com",
    url="https://github.com/PaesslerAG/django-rosetta-grappelli",
    packages=find_packages(),
    install_requires=[
        'django-rosetta>=0.8.1',
        'Django>=1.8, <2.1',
    ],
    include_package_data=True,
)
