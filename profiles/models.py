from django.contrib.auth import get_user_model
from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save


def upload_location(instance, filename):
    location = str(instance.user.username)
    return f"{location}/{filename}"


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    location = models.CharField(max_length=120, null=True, blank=True)
    picture = models.ImageField(
        upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("profile", kwargs={"username": self.user.username})

    def like_link(self):
        return reverse("like_user", kwargs={"id": self.user.id})


class UserJob(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    position = models.CharField(max_length=220)
    location = models.CharField(max_length=220)
    employer_name = models.CharField(max_length=220)

    def __str__(self):
        return self.position


from jobs.models import Location, Job, Employer


def post_save_user_job(sender, instance, created, *args, **kwargs):
    job = instance.position.lower()
    location = instance.location.lower()
    employer_name = instance.employer_name.lower()
    # Job.objects.get(text__iexact=job)
    # case insenstive Cashier or cashier
    new_job = Job.objects.get_or_create(text=job)
    new_location, created = Location.objects.get_or_create(name=location)
    new_employer = Employer.objects.get_or_create(
        location=new_location, name=employer_name)


post_save.connect(post_save_user_job, sender=UserJob)
