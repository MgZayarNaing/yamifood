from django.db import models

# Create your models here.

class Imageslider(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Startabout(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()

    def __str__(self):
        return self.title


class Gallery(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Gallery/')

    def __str__(self):
        return self.name


class CustomerReviews(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='CustomerReviews/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Information(models.Model):
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    location = models.TextField(max_length=200)

    def __str__(self):
        return self.phone

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Menu(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name='categories')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=20)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name



