# Generated by Django 4.2 on 2023-04-18 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_cust", "0005_alter_customuser_managers"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogger",
            name="password",
        ),
    ]