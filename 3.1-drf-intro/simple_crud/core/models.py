from django.db import models
from django.utils.translation import gettext as _


class Dated(models.Model):
    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, verbose_name=_('Created'),
        db_index=True
    )
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, verbose_name=_('Updated'),
        db_index=True
    )

    class Meta:
        abstract = True
