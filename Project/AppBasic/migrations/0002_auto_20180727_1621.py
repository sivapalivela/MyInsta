# Generated by Django 2.0.7 on 2018-07-27 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppBasic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='ProfilePic',
            new_name='Profile_Pic',
        ),
        migrations.RenameField(
            model_name='useraccount',
            old_name='YourWebsite',
            new_name='Your_Website',
        ),
    ]
