from setuptools import setup, find_packages

setup(
    name="pdf-combine",
    version="0.1.0",
    description="A command-line tool to n-up PDF pages",
    author="Thameera Senanayaka",
    author_email="me@thameera.com",
    packages=find_packages(),
    install_requires=[
        "pypdf",
    ],
    entry_points={
        "console_scripts": [
            "pdf-combine=pdf_combine.cli:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
