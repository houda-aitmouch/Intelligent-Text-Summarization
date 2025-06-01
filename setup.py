import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.1.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "Houda Aitmouch"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "aitmouchhouda4@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/houda-aitmouch/Intelligent-Text-Summarization.git",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)