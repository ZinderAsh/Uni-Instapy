import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instapy",
    version="1.0.0",
    author="sindreve",
    author_email="sindreve@ifi.uio.no",
    description="instagram filters in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.uio.no/IN3110/IN3110-sindreve/tree/master/assignment4",
    packages=["instapy", "tests"],
    scripts=["bin/instapy"],
    setup_requires=["numpy", "setuptools>=18.0"],
    install_requires=["numpy", "numba", "opencv-python"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)