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


class ContactMessages(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()

    def __str__(self):
        return self.email

    class  Meta: 
        verbose_name_plural  =  "Contact Messages"
