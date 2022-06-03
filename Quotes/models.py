from django.db import models

# Create your models here.


class Random_Quotes(models.Model):
    Quote = models.CharField(max_length=100)
    Author = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return f"{self.Quote}"
