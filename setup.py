from setuptools import setup

setup(
    name='kubiki',
    version='1.0',
    author='Konstantin Ilyashenko',
    packages=['kubiki'],
    description='Education enviroment in Minecraft style',
    entry_points={'console_scripts': ['kubiki = kubiki.space:run']},
    install_requires=['pyglet', 'mcpi', 'minecraftstuff']
)
