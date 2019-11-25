import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='penut85420',
    version='1.0.0',
    author='PenutChen',
    author_email='penut85420@gmail.com',
    description='Hello, python package',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/penut85420/TestingPythonPackage',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)