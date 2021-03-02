import pathlib
from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="couscous",
    version="0.0.1",
    description="Experimental specification enabler.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/sthagen/improved-couscous",
    author="Stefan Hagen",
    author_email="stefan@hagen.link",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="specification actionable enhance development",
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        "attrs",
    ],
    entry_points={
        "console_scripts": [
            "couscous=couscous.cli:main",
        ]
    },
)

