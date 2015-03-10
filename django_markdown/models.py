from django.db import models
from .fields import MarkdownFormField
from .widgets import MarkdownWidget

try:
	from south.modelsinspector import add_introspection_rules
	add_introspection_rules([], ["^django_markdown\.models\.MarkdownField"])
except ImportError:
	# South is not installed, so we need not add an introspection rule.
	pass

class MarkdownField(models.TextField):
    def formfield(self, **kwargs):
        defaults = {'form_class': MarkdownFormField}
        defaults.update(kwargs)
        return super(MarkdownField, self).formfield(**defaults)
