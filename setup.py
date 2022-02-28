from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'A wrapper for the giphy public API'
LONG_DESCRIPTION = 'A package wrapper for the giphy public API that allows you to work with Giphy API endpoints.'

# Setting up
setup(
    name="easygiphy",
    version=VERSION,
    author="barii.py (K.Khademul Bari)",
    author_email="<barii.py@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'giphy', 'giphy api', 'gif'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)