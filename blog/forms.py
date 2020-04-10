from django import forms

from .models import PostFile

class PostFileForm(forms.ModelForm):
    # def __init__(self, qs=None, *args, **kwargs):
    #     super(PostFileForm, self).__init__(*args, **kwargs)
    #     self.fields['shared_with'].widget = forms.CheckboxSelectMultiple()

    class Meta:
        model = PostFile
        fields = ['title', 'expiration','content','file']
        # fields = ['title', 'expiration','content','file','shared_with']
        widgets = {
            'file': forms.FileInput(attrs={ 'class': 'form-control', 'multiple': True})
        }