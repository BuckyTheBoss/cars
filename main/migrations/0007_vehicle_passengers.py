# Generated by Django 3.2.6 on 2021-08-18 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_imageprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='passengers',
            field=models.ManyToManyField(related_name='in_cars', to='main.Person'),
        ),
    ]
