## **Full wolf but sheep dead**

Program that simulates wolf chasing and murdering sheep, done for learning purposes to subject "Python programming".

### Authors

Maciej Błażewicz\
Sebastian Nawrocki

### TUL 2020/21

##### Create a package:

- If you don't have wheel package installed, install it with a command:
```pip install wheel```
- Create setup.py file with configuration of package
- Run setuptool command: 
```python setup.py sdist bdist_wheel```

#### Create a virtual environment
- Run command to create venv: 
```python -m venv venv_name```
- Activate venv: 
```.\venv_name\Scripts\activate```
- Deactivate venv:
```deactivate```

##### Install the package in the virtual environment

- Install the package: 
```pip install dist\package_name.whl --force-reinstall```
- Use --force-reinstall option, if you have installed new package with the same version.
- Import the package: 
```import package_name```

##### Run a console application in the virtual environment.

- Run a command: 
```python -m chase [ARGS]```
