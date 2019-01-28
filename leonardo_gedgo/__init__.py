
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_gedgo.Config'


LEONARDO_APPS = ['gedgo', 'leonardo_gedgo']
LEONARDO_PLUGINS = [
    ('leonardo_gedgo.apps.gedgo', _('Gedgo')),
]
LEONARDO_WIDGETS = [
    'leonardo_gedgo.widget.families.models.FamiliesWidget'
]


class Config(AppConfig):
    name = 'leonardo_gedgo'
    verbose_name = "leonardo-gedgo"
