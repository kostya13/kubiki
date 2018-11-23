from setuptools import setup

setup(
    name='Kubiki',
    version='1.0',
    author='Konstantin Ilyashenko',
    packages=['kubiki'],
    description='Education enviroment in Minecraft style',
    entry_points={'console_scripts': ['kubiki = kubiki:show']},
    install_requires=['pyglet']
)
