from django import forms

from .models import PostFile

class PostFileForm(forms.ModelForm):
    class Meta:
        model = PostFile
        fields = ['title', 'expiration','content','file']
        widgets = {
            'file': forms.FileInput(attrs={ 'class': 'form-control', 'multiple': True})
        }