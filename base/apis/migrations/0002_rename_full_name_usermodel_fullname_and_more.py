# Generated by Django 5.0.6 on 2024-06-25 07:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermodel',
            old_name='full_name',
            new_name='fullName',
        ),
        migrations.RenameField(
            model_name='usermodel',
            old_name='phone_no',
            new_name='phoneNumber',
        ),
    ]
