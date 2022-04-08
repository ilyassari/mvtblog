from django import forms

from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from blog.models import CategoryModel, PostModel

class AddPostForm(forms.Form):
    """docstring for Add Post Form."""
    title = forms.CharField(label='Başlık', min_length=1, max_length=30)
    image = forms.ImageField(label='Kapak Resmi', required=False)
    categories = forms.MultipleChoiceField(
        label='Kategoriler',
        choices=list(category for category in CategoryModel.objects.values_list('id', 'title')),
        widget=forms.CheckboxSelectMultiple()
    )
    content = forms.CharField(widget=CKEditorUploadingWidget())

class UpdatePostForm(forms.Form):
    """docstring for Add Post Form."""
    title = forms.CharField(label='Başlık', min_length=1, max_length=30)
    image = forms.ImageField(label='Kapak Resmi', required=False)
    categories = forms.MultipleChoiceField(
        label='Kategoriler',
        choices=list(category for category in CategoryModel.objects.values_list('id', 'title')),
        widget=forms.CheckboxSelectMultiple()
    )
    content = forms.CharField(widget=CKEditorUploadingWidget())
