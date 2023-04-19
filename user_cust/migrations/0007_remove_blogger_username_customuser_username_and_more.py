# Generated by Django 4.2 on 2023-04-18 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_cust", "0006_remove_blogger_password"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blogger",
            name="username",
        ),
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="blogger",
            name="bio",
            field=models.CharField(default="", max_length=200),
        ),
    ]
