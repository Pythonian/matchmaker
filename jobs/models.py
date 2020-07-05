from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify


class Job(models.Model):
    text = models.CharField(max_length=120, unique=True)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(get_user_model(), blank=True)

    def __str__(self):
        return self.text

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Location(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField()
    active = models.BooleanField(default=True)
    flagged = models.ManyToManyField(get_user_model(), blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Employer(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
