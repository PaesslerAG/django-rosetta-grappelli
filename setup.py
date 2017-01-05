from setuptools import setup, find_packages

setup(
    name="django-rosetta-grappelli2",
    version="1.1",
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
    ],
    include_package_data=True,
)
