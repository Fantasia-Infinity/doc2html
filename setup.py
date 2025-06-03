#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages

# 读取 README 文件
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取版本信息
version = {}
with open("doc2html/__version__.py", "r", encoding="utf-8") as fh:
    exec(fh.read(), version)

setup(
    name="doc2html",
    version=version["__version__"],
    author="Fantasia-Infinity",
    author_email="",
    description="A tool to convert Markdown documents to HTML with beautiful styling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Fantasia-Infinity/doc2html",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'doc2html': ['templates/*.html'],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Documentation",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Text Processing :: Markup :: Markdown",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "markdown>=3.0.0",
        "pygments>=2.0.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "twine>=3.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "doc2html=doc2html.cli:main",
            "md2html=doc2html.cli:main",
        ],
    },
    keywords="markdown html converter documentation",
    project_urls={
        "Bug Reports": "https://github.com/Fantasia-Infinity/doc2html/issues",
        "Source": "https://github.com/Fantasia-Infinity/doc2html",
        "Documentation": "https://github.com/Fantasia-Infinity/doc2html#readme",
    },
)
