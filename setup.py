from setuptools import setup, find_packages

packages = (find_packages(exclude=["Old_Stuff*", "bk_programs*", "Arthur_website*"]),)

setup(
    # Package name
    packages=find_packages(),
    install_requires=[
        "sentence_transformers>=2.3.1",
        "scikit-learn>=1.3.1",
        "numpy>=1.24.2",
        "nltk>=3.8.1",
        "colorama>=0.4.6",
        "flask>=3.0.0",
        "matplotlib>=3.7.0",
        "transformers>=4.37.2",
        "torch>=2.0.0",
    ],
)
