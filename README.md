## django-multi-fk

In order to explain what this package does and the problem it solves, consider the following models:

    class Something(models.Model):
        pass

    class Someone(models.Model):
        thing1 = models.ForeignKey(Something, related_name='+')
        thing2 = models.ForeignKey(Something, related_name='+')

Registering both of these models in the Django admin results in the following `<select>` fields:

![Django Admin](http://i.stack.imgur.com/JgJQ7.png)

Clicking the "+" next to "Thing1" causes a popup window to open which can be used to add a new item. Once the popup is dismissed, the new item appears in the `<select>` for "Thing1" **but not in the `<select>` for "Thing2"**. This is the problem that django-multi-fk attempts to solve.
