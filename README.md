# Hello
+ This is a testing repo.

## Steps
1. Installing packages.
    ```
    python -m pip install setuptools wheel twine
    ```
2. Building the distribution archieves.
    ```
    python setup.py sdist bdist_wheel
    ```
3. Uploading the distribution archieves.
    ```
    python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```