from django import forms


class AddCommentForm(forms.Form):
    """docstring for Add Post Form."""
    content = forms.CharField(label='Yorumunuz', widget=forms.Textarea())
