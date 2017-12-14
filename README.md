Django app for choices with autocomplete and good readability

## Installation

For python<=3.4 install [enum34](https://pypi.python.org/pypi/enum34):

```bash
sudo pip install enum34
```

Install this module:

```bash
sudo pip install -e git+https://github.com/orsinium/djchoices.git#egg=djchoices
```

## Example

```ipython
In [1]: from djchoices import Choices

In [2]: class SOURCES(Choices):
   ...:     IOS = 'i', 'iOS app'
   ...:     ANDROID = 'a', 'Android app'

In [3]: SOURCES.choices()
Out[3]: (('a', 'Android app'), ('i', 'iOS app'))

In [4]: SOURCES.IOS.verbose
Out[4]: 'iOS app'

In [5]: Sources.IOS.db
Out[5]: 'i'
```

```python
source = models.CharField(max_length=1, choices=SOURCES.choices())
```
