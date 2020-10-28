from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    name = models.CharField(max_length=100)
    tag_slug = models.SlugField()

    def __str__(self):
        return self.name

class Service(models.Model):
    h1 = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    intro = models.TextField()
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    content = RichTextUploadingField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')
    image = models.FileField(upload_to='blog')

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.pk} {self.title}'


