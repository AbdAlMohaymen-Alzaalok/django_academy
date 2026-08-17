from django import forms
from . import models

attrs={'class':'form-control'}

class CommentFrom(forms.ModelForm):
    class Meta:
        model=models.Comment
        fields=['content']
        widgets={
            'content':forms.TextInput(attrs=attrs)
        }