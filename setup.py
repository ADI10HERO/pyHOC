import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="applied_maths-adi10hero",
    version="0.0.2",
    author="Aditya Srivastava",
    author_email="adityasrivastava301199@gmail.com",
    description="Calculates Higher Order Crossings of a signal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ADI10HERO/pyHOC",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    test_suite='nose.collector',
    tests_require=['nose'],
)
