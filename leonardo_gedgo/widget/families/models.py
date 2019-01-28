# -#- coding: utf-8 -#-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from leonardo.module.web.models import ListWidget
from gedgo.models import Family
from leonardo.forms.fields import ModelSelect2MultipleWidget


class FamiliesWidget(ListWidget):

    widgets = {
        'families': ModelSelect2MultipleWidget(
            queryset=Family.objects.all(),
            search_fields=['husbands__first_name__icontains',
                           'husbands__last_name__icontains',
                           'wives__first_name__icontains',
                           'wives__last_name__icontains'])
    }

    # feincms_item_editor_form = KeyFamilyWidgetForm

    families = models.ManyToManyField(
        'gedgo.Family',
        related_name='gedgo_widget_families',
        blank=True
    )

    def get_items(self, **kwargs):
        items = []
        for family in self.families.all():
            items += list(family.spouses)
        return items

    class Meta:
        abstract = True
        verbose_name = _('family')
        verbose_name_plural = _('families')
