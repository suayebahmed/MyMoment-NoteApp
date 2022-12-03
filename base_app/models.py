from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

# Moment table
class Moment(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=20)
    # text = models.TextField()
    text = RichTextField(blank=True, null=True)

    def __str__(self):
        return str(self.id)+ ".  " + self.title 

    def get_absolute_url(self):
        # return reverse('moment-detail-page', args=(str(self.pk)))
        return reverse('home-page')

