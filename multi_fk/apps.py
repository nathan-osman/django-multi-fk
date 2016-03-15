from django.apps import AppConfig
from django.contrib.admin.options import ModelAdmin
from django.forms import Media


class MultiFkConfig(AppConfig):
    name = 'multi_fk'

    def ready(self):
        """
        Monkey-patch the ModelAdmin.media property in order to ensure the
        multi_fk.js file is included in admin pages.
        """

        old_media = ModelAdmin.media

        def new_media(self):
            return old_media.__get__(self) + Media(js=[
                'admin/js/multi_fk.js',
            ])

        ModelAdmin.media = property(new_media)
