from django import forms
from django.contrib.auth.models import User
from .models import PostFile,share
from django.contrib.auth.models import User

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


class PostFileShareForm(forms.ModelForm):
    class Meta:
        model = share
        fields = ['viewer_username']
        
    def clean(self):
        cleaned_data = super().clean()
        u_name = cleaned_data.get('viewer_username')
        try:
            user = User.objects.get(username=u_name)
        except User.DoesNotExist:
            user = None

        if user == None :
            raise  forms.ValidationError('Please enter a correct username. Note that field may be case-sensitive.')
