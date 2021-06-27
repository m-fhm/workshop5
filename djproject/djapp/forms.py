from django import forms
from . models import usermodel

class userforms(forms.ModelForm):
    # subject = forms.CharField(max_length=100)
    # message = forms.CharField(widget=forms.Textarea)
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)
    
    class Meta:
        model= usermodel
        fields = '__all__'
        # fields = ['name','email']
        # exclude = ['name']
