import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "taps",
    packages = setuptools.find_packages(),
    version = "0.1.0",
    description = "True Arch package security - audit and query packages",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Vimru/taps",
    install_requires = [
        "colorful"
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    python_requires = ">=3.6",
    include_package_data = True,
    license = "GPLv3",
    scripts = ["bin/taps"],
)
