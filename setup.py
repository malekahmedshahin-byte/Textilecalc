from setuptools import setup, find_packages

setup(
    name="textilecalc",
    version="2.0.0",
    author="Abdul Malek",
    author_email="",
    description=(
        "A complete Python library for textile engineering calculations. "
        "v2.0 adds AI yarn count recommender, shade recipe predictor, "
        "and carbon footprint calculator."
    ),
    long_description=open("README.md", "r", encoding="utf-8").read()
        if __import__("os").path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    url="https://github.com/malekahmedshahin-byte/Abdul-Malek",
    packages=find_packages(),
    install_requires=[],          # zero external dependencies — pure Python
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Intended Audience :: Education",
        "Intended Audience :: Manufacturing",
    ],
    keywords=(
        "textile engineering yarn fabric dyeing spinning weaving calculations "
        "carbon footprint sustainability shade recipe color matching"
    ),
)
