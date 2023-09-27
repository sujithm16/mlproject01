import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "end2endmlproject"
AUTHOR_USER_NAME = "sujithm16"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "sujithm1610@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


# 6 files are common for all the projects for now. template.py,setup.py,
# requirements.txt(content may vary),utils-common.py,logging-__init__.py,
# constants-__init__.py