import io
from os import path

from setuptools import setup, find_packages

import vkteams

here = path.abspath(path.dirname(__file__))


def long_description():
    with io.open(file=path.join(here, "README.md"), encoding="utf-8") as file:
        return file.read()


def requirements():
    with io.open(file=path.join(here, "requirements.txt")) as file:
        return file.readlines()


setup(
    name="vkteams",
    version=vkteams.__version__,
    description="Pure Python interface for Bot API. Bot cookbook for Humans.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/alex3ysmirnov/vkteams",
    author="alex3ysmirnov",
    author_email="alex3ysmirnov@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent"
    ],
    keywords="mailru im bot api postmaster alex3ysmirnov vkteams vk teams",
    packages=find_packages(exclude=["example"]),
    install_requires=requirements(),
    python_requires=">= 2.7, != 3.0.*, != 3.1.*, != 3.2.*, != 3.3.*",
    include_package_data=True,
    zip_safe=False
)
