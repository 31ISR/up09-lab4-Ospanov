from django import forms
from . import models

class CreateCommunities(forms.ModelForm):
    class Meta:
        model = models.Community
        fields = ['name','description','slug','avatar']
