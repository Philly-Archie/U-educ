# Generated by Django 5.0.6 on 2024-06-13 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('u_educ_site', '0004_sponsorpreferences_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sponsorpreferences',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
        migrations.RenameField(
            model_name='sponsorpreferences',
            old_name='profile_image',
            new_name='profileImage',
        ),
        migrations.RenameField(
            model_name='sponsorpreferences',
            old_name='zip_code',
            new_name='zipCode',
        ),
    ]
