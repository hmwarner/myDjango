from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from multiselectfield import MultiSelectField
from django.utils.text import slugify

class SocialLink(models.Model):
    link_name = models.CharField(max_length=100,verbose_name='Link Name')
    link_url = models.CharField(max_length=250,verbose_name='URL')
    link_created_date = models.DateTimeField(default=timezone.now,verbose_name='Link Created')

    def clean_title(self):
        return self.title.capitalize()

class Tag(models.Model):
    title = models.CharField(max_length=75, verbose_name='Tag')
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def get_absolute_url(self):
        return reverse('tags', args=[self.slug])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=66)
    image = models.ImageField(upload_to='preview_photos', verbose_name='Caption Image')
    content = RichTextUploadingField(config_name='default',null=True)
    tags = models.ManyToManyField(Tag, related_name='tags')
    date_posted = models.DateTimeField(default=timezone.now,verbose_name='Date Posted')

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
