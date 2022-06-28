from setuptools import setup, find_packages

from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='kivyx',
    packages=find_packages(
            include=["kivyx","kivyx.*"]
        ),
    package_data={
        'kivyx': [
            'data/*.png',
            'data/*.jpg',
            'data/*.ttf',
            'editor/*.py',
            'fonts/*.ttf',
        ]
    },
    include_package_data=True,
    version='0.0.2',
    description='An UI library for personal projects',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Yunus Ceyhan',
    author_email='yunus.ceyhn@gmail',
    url='https://github.com/kivyx',
    keywords=['Python', 'Kivy', 'KivyMD'],
    install_requires=["kivy","pygments"],
    classifiers=[],
)
