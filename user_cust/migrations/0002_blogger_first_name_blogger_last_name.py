# Generated by Django 4.2 on 2023-04-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_cust", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogger",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AddField(
            model_name="blogger",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
    ]
