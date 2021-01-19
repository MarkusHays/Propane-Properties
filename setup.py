from setuptools import find_packages
from setuptools import setup

setup(
    name="propane_properties",
    version="0.0.1",
    url="https://github.com/MarkusHays/Propane-Properties",
    license="GPL-3.0",
    author="Markus Hays Whitson",
    description=(
        "This program calculates the density of propane for both "
        "liquid and vapor phase using the modified Benedict-Webb-Ruben "
        "EOS proposed by Starling in his book 'Fluid Thermodynamic "
        "Properties for Light Petroleum Systems'"
    ),
    packages=find_packages(exclude=("tests",)),
    install_requires=["scipy", "numpy", "matplotlib"],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
