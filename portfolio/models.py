from django.db import models


class Enquiry(models.Model):
    sender = models.CharField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
