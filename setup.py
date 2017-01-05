from setuptools import setup, find_packages

setup(
    name="django-rosetta-grappelli2",
    version="1.1",
    description="""
    Compatibility templates for django rosetta when using django-grappelli
    """,
    author="Platypus Creation",
    author_email="contact@platypus-creation.com",
    url="https://github.com/belugame/django-rosetta-grappelli",
    packages=find_packages(),
    install_requires=[
        'django-rosetta>=0.6.5',
    ],
    include_package_data=True,
)
