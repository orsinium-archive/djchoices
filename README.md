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

Definition:

```python
from djchoices import Choices

class SOURCES(Choices):
    IOS = 'i', 'iOS app'
    ANDROID = 'a', 'Android app'
```

Usage in models:

```python
source = models.CharField(max_length=1, choices=SOURCES.choices())
```

Manual usage:

```python
SOURCES.choices()
# (('a', 'Android app'), ('i', 'iOS app'))

SOURCES.IOS
# <SOURCES.IOS: ('i', 'iOS app')>

SOURCES.IOS.verbose
# 'iOS app'

SOURCES.IOS.db
# 'i'

SOURCES.IOS.name
# 'IOS'

SOURCES.IOS.value
# ('i', 'iOS app')

SOURCES.by_db('i')
# <SOURCES.IOS: ('i', 'iOS app')>

SOURCES.by_verbose('iOS app')
# <SOURCES.IOS: ('i', 'iOS app')>

SOURCES.verbose_by_db('i')
# 'iOS app'

SOURCES.db_by_verbose('iOS app')
# 'i'
```
