import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name="penut85420", # Replace with your own username
    version="0.0.1",
    author="PenutChen",
    author_email="penut85420@gmail.com",
    description="Hello, python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)