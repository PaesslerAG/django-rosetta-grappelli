from setuptools import setup, find_packages

with open('VERSION', 'r') as f:
    version = f.read().strip()

setup(
    name="django-rosetta-grappelli2",
    version=version,
    description="""
    Compatibility templates for django rosetta when using django-grappelli. Continued
    development from the original but stalled django-rosetta-grappelli project.
    """,
    author="Martin Bauer",
    author_email="info@beluga.me",
    url="https://github.com/belugame/django-rosetta-grappelli",
    packages=find_packages(),
    install_requires=[
        'django-rosetta>=0.6.5',
        'Django>=1.5,<1.9',
    ],
    include_package_data=True,
)
