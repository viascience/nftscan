import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="nftscan",
    version="0.1.0",
    description="NFT scanner to ensure your favorite NFT doesnt contain malware",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/viascience/architectural-decision-artifacts",
    author="Jesus Cardenes",
    author_email="jcardenes@solvewithvia.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8.3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "realpython=nftscan.__main__:main",
        ]
    },
)

