# Generated by Django 3.0.8 on 2021-12-31 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quotes', '0003_auto_20211231_1030'),
    ]

    operations = [
        migrations.AddField(
            model_name='random_quotes',
            name='Author',
            field=models.CharField(default='Unknown', max_length=100000),
        ),
    ]
