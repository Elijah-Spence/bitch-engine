from setuptools import setup, find_packages

setup(
    name="bitch-engine",
    version="3.0.0",
    author="VINCULA / GARY",
    author_email="gary@slime.dev",
    description="B.I.T.C.H. v3 — Self-healing, multi-language code execution engine. Never fails.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/vincula/bitch_engine",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Compilers",
    ],
    python_requires=">=3.8",
    extras_require={
        "polyglot": ["polyglot"],
        "polymorphic": ["polymorphic"],
        "universal": ["universal_translator"],
        "all": ["polyglot", "polymorphic", "universal_translator"],
    },
    entry_points={
        "console_scripts": [
            "bitch=bitch_engine:main",
        ],
    },
)
