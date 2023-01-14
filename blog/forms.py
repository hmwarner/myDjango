from django import forms
from .models import Post
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = [
            'title',
            'tags',
            'image',
            'content',
            ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'] = forms.CharField(
                                required=True,
                                label='Article Title',
                              )
        self.fields['tags'] = forms.CharField(
                                required=False,
                                label='Tags',
                              )
        self.fields['image'] = forms.ImageField(
                                required=True,
                                label='Caption Image',
                              )
        self.fields['content'] = forms.CharField(
                            required=True,
                            label='Article Content',
                            widget=CKEditorUploadingWidget(config_name='default'),
                            )
