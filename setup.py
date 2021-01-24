"""
This application conjugates the verbs of multiple languages
Copyright (C) 2020 Konjugators
See LICENSE for more information
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="console-conjugator",
    version="0.1.3",
    author="Konjugators",
    author_email="shynn.lawrence@gmail.com",
    description="Versatile command line conjugator for german",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Konjugators/console-conjugator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: German",
        "Natural Language :: French",
        "Environment :: Console :: Curses",
        "Topic :: Education", 
        "Environment :: Console",
    ],
    python_requires=">=3.4",
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "konjugier=Conjugator.deutschCLI:main",
            "conjuguer=Francaisconjugation.cli_scripts:main"
        ]
    },
)
