from django.db import models

# Create your models here.


class Random_Quotes(models.Model):
    Quote = models.CharField(max_length=2000)
    Author = models.CharField(max_length=1000, default='Unknown')

    def __str__(self):
        return f"{self.Quote}"
