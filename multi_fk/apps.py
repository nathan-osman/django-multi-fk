from django.apps import AppConfig
from django.contrib.admin.widgets import RelatedFieldWidgetWrapper
from django.forms import Media


class MultiFkConfig(AppConfig):
    name = 'multi_fk'

    def _patch_widget(self):
        """
        Monkey-patch the RelatedFieldWidgetWrapper widget in order to add the
        "data-model" attribute, indicating which model the field links to.
        """

        old_render = RelatedFieldWidgetWrapper.render

        def new_render(self, *args, **kwargs):
            kwargs['attrs']['data-model'] = self.rel.model._meta.db_table
            return old_render(self, *args, **kwargs)

        RelatedFieldWidgetWrapper.render = new_render

    def _patch_media(self):
        """
        Monkey-patch the RelatedFieldWidgetWrapper.media property in order to
        ensure the multi_fk.js file is included in admin pages.
        """

        old_media = RelatedFieldWidgetWrapper.media

        def new_media(self):
            return old_media.__get__(self) + Media(js=[
                'admin/js/multi_fk.js',
            ])

        RelatedFieldWidgetWrapper.media = property(new_media)

    def ready(self):
        self._patch_widget()
        self._patch_media()
