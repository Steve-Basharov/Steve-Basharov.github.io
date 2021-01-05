from .models import job
from django.forms import ModelForm, TextInput, Textarea

class job_form(ModelForm):
    class Meta:
        model = job
        fields = ['tg', 'cash', 'tex_zad']
    