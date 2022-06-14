from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=250)
    relationship = models.CharField(max_length=250, null=True, blank=True)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.full_name
