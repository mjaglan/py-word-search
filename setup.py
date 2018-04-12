from distutils.core import setup

setup(
    # Application name:
    name="word_search",

    # Version number (initial):
    version="0.0.1.20180411",

    # Application author details:
    author="Mayank Jaglan",
    author_email="mjaglan@umail.iu.edu",

    # Packages
    packages=["word_search"],

    # Details
    url="http://pypi.python.org/pypi/word_search_v001/",

    license="LICENSE",

    description="Given a dictionary, list all meaningful words in N x M grid of characters.",

    long_description=open("README.txt").read(),

    platforms='any',

)
