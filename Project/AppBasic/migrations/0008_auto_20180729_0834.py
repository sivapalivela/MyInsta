# Generated by Django 2.0.7 on 2018-07-29 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBasic', '0007_auto_20180728_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datamodel',
            name='Describe',
            field=models.CharField(max_length=1024),
        ),
    ]