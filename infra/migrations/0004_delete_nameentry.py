# Generated by Django 4.2.7 on 2024-11-05 04:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("infra", "0003_nameentry"),
    ]

    operations = [
        migrations.DeleteModel(
            name="NameEntry",
        ),
    ]
