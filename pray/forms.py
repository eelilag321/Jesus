from django.forms import ModelForm
from . models import Prayer
from django.utils.translation import gettext_lazy as _

class PrayerCreateForm(ModelForm):
    class Meta():
        model = Prayer
        fields = ['name', 'content']
        labels = {
            'name': _('Your name'),
            'content': _('What you hope for'),
        }