from setuptools import setup

setup (
        name="thonny-kubiki",
        version="1.0",
        author="Aivar Annamaa",
        author_email="aivar.annamaa@gmail.com",
        python_requires=">=3.5",
        install_requires=["thonny>=3.0.0"],
        packages=["thonnycontrib.kubiki"]
)