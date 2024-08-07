# Generated by Django 5.0.6 on 2024-06-22 08:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('u_educ_site', '0006_remove_sponsorpreferences_profileimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsorpreferences',
            name='tuition_amount_max',
            field=models.DecimalField(blank=True, decimal_places=2, help_text='Maximum tuition amount the sponsor is willing to provide.', max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
