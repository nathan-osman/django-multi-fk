## django-multi-fk

[![License](http://img.shields.io/badge/license-MIT-yellow.svg)](http://opensource.org/licenses/MIT)
[![PyPI Version](http://img.shields.io/pypi/v/django-multi-fk.svg)](https://pypi.python.org/pypi/django-multi-fk)
[![PyPI Downloads](http://img.shields.io/pypi/dm/django-multi-fk.svg)](https://pypi.python.org/pypi/django-multi-fk)

In order to explain what this package does and the problem it solves, consider the following models:

    class Something(models.Model):
        pass

    class Someone(models.Model):
        thing1 = models.ForeignKey(Something, related_name='+')
        thing2 = models.ForeignKey(Something, related_name='+')

Registering both of these models in the Django admin results in the following `<select>` fields:

![Django Admin](http://i.stack.imgur.com/JgJQ7.png)

Clicking the "+" next to "Thing1" causes a popup window to open which can be used to add a new item. Once the popup is dismissed, the new item appears in the `<select>` for "Thing1" **but not in the `<select>` for "Thing2"**. This is the problem that django-multi-fk attempts to solve.

### Installation

The easiest way to install the package is by using:

    pip install django-multi-fk

Once installed, simply add `multi_fk` to `INSTALLED_APPS` in `settings.py`:

    INSTALLED_APPS = [
        #...
        'multi_fk',
    ]
    
