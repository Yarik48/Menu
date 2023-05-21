from django.db import models
from django.urls import reverse


class Post(models.Model):
    text = models.CharField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('details_post', kwargs={'post_id': self.pk})

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.TextField()

    def get_absolute_url(self):
        return reverse('details_category', kwargs={'category_id': self.pk})

    def __str__(self):
        return f"{self.name}"