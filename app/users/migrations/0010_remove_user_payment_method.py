# Generated by Django 4.0.10 on 2024-03-14 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_user_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='payment_method',
        ),
    ]
