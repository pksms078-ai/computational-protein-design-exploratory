from setuptools import setup, find_packages

setup(
    name="computational-protein-design-exploratory",
    version="0.3.0",
    author="Prabin Kumar",
    author_email="prabincheslind@gmail.com",
    description="Exploratory computational protein design framework using ML and molecular simulation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/pksms078-ai/computational-protein-design-exploratory",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "tensorflow",
        "mdtraj",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
)
