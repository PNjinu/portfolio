from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.summary
    

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=200)
    cont = models.CharField(max_length=350)
    link = models.URLField(max_length = 200)

    def __str__(self):
        return self.title
