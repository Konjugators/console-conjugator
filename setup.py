import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="console-conjugator",
    version="0.0.4",
    author="Shynn Lawrence & Govind Gnanakumar",
    author_email="shynn.lawrence@gmail.com",
    description="Deutsch command line conjugator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sandkoan/console-conjugator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
    include_package_data=True,
)
