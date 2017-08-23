from .models import Article
from ckeditor_uploader.fields import RichTextUploadingFormField
from django import forms


class ReportForm(forms.Form):
    date = forms.DateField()


class ArticleForm(forms.ModelForm):
    # status = forms.CharField(widget=forms.HiddenInput())
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255)
    tags = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        max_length=255, required=False,
        help_text='Use spaces to separate the tags, such as "java jsf primefaces"')  # noqa: E501

    class Meta:

        model = Article
        fields = ('title', 'content', 'tags', 'publish')
