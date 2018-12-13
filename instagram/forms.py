from django import forms
from .models import *

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['name']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post_by','post']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['comments']
