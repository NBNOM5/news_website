from django import forms
from .models import Comment

class ShareForm(forms.Form):
    name  = forms.CharField(max_length=50)
    email = forms.EmailField()
    to  = forms.EmailField()
    comment = forms.CharField(max_length=250, required=False)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


        