# Foobar

Foobar is a Python library for dealing with word pluralization.

## Installation
Pylint is a Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions. 
Pylint can be simply installed by running:

pip install pylint
If you are using Python 3.6+, upgrade to get full support for your version:

pip install pylint --upgrade
If you want to install from a source distribution, extract the tarball and run the following command

python setup.py install

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install foobar
```

## Usage

```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
