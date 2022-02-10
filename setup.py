from setuptools import setup, find_packages

BUILD_REQUIREMENTS = [
    "black==22.*,>=22.1.0",
    "pre-commit==2.*,>=2.17.0",
]

RUNTIME_REQUIREMENTS = []

ALL_REQUIREMENTS = BUILD_REQUIREMENTS + RUNTIME_REQUIREMENTS

TESTS_REQUIREMENTS = [
    "pytest==7.*,>=7.0.0",
    "pytest-cov==3.*,>=3.0.0",
]

setup(
    name="stupy",
    version="0.0.1",
    author="Raphael Rossi",
    description=("Study python project"),
    license="MIT",
    keywords="python study",
    url="https://github.com/RaphaelVRossi/stupy",
    packages=find_packages(),
    long_description="Long",
    classifiers=[
        "Development Status :: 1 - Planning",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    install_requires=RUNTIME_REQUIREMENTS,
    extras_require={
        "all": ALL_REQUIREMENTS,
        "tests": ALL_REQUIREMENTS + TESTS_REQUIREMENTS,
    },
)
