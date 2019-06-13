from django import forms

from .models import post


class postForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
        }
    ))

    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ))


    class Meta:
        model = post
        fields = ( 'title', 'text',)