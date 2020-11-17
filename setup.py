import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="console-conjugator",
    version="0.1.1",
    author="Shynn Lawrence, Aditya Matam, Govind Gnanakumar",
    author_email="shynn.lawrence@gmail.com",
    description="Versatile German command line conjugator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Konjugators/console-conjugator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.4",
    include_package_data=True,
    entry_points={"console_scripts": ["konjugier=Deutschconjugation.cli_scripts:main"]},
)
