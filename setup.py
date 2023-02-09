from setuptools import setup, find_packages
import os


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


def get_version():
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "cloudcaddy", "version.py"
    )
    g = {}
    with open(path) as fp:
        exec(fp.read(), g)
    return g["__version__"]


setup(
    name="cloudcaddy",
    version=get_version(),
    description="An open source multi-tool for exploring and publishing data",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    license="Apache License, Version 2.0",
    url="https://cloudcanvas.xyz",
    project_urls={
        "Documentation": "https://docs.cloudcaddy.io/en/stable/",
    },
    packages=find_packages(exclude=("tests",)),
    package_data={"cloudcaddy": ["templates/*.html"]},
    include_package_data=False,
    python_requires=">=3.9",
    install_requires=[
        "requests>=2.28.0",
    ],
    entry_points="""
        [console_scripts]
        cloudcaddy=cloudcaddy.cli
    """,
    setup_requires=["pytest-runner"],
    extras_require={
        "docs": [
        ],
        "test": [
            "pytest>=5.2.2",
        ],
        "rich": ["rich"],
    },
    tests_require=["cloudcaddy[test]"],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.10",
    ],
)
