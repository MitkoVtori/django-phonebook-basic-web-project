from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=13)