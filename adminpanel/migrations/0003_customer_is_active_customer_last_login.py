# Generated by Django 5.1.3 on 2024-11-24 16:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0002_alter_customer_email_alter_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
