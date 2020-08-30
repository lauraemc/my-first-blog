from django.conf import settings
from django.db import models
from django.utils import timezone

#Defines model - as on object called Post
#foreignKey - link to another model

class Post(models.Model):
   
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text_preview = models.TextField(blank=True)
    text = models.TextField()
    image_path = models.TextField(blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class WorkElement(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    dates = models.TextField()
    employer = models.TextField()
    location = models.TextField()
    position = models.TextField()
    assignments = models.TextField()
    paid = models.BooleanField()
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def assignments_as_list(self):
        return self.assignments.split('\n')

    def __str__(self):
        return self.employer

class EduElement(models.Model):
    dates = models.TextField()
    title = models.TextField()
    subTitle = models.TextField()
    text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def text_as_list(self):
        return self.text.split('\n')

    def __str__(self):
        return self.title 

class Skills(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    fluent = models.TextField()
    experience = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Extra(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    