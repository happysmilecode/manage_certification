# Generated by Django 3.0.5 on 2023-06-28 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pic/Customer/lazy.PNG', null=True, upload_to='profile_pic/Customer/'),
        ),
    ]
