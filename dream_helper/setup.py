from setuptools import setup, find_namespace_packages

setup(
    name='dream_helper',
    version='1',
    description='Address Book, Notes and other',
    url='https://github.com/Sedigor/drem_team',
    packages=find_namespace_packages(),
    #install_requires=['markdown'],
    entry_points={'console_scripts': ['dthelper = dream_helper.main:main']}
)