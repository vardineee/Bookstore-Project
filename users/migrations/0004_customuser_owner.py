# Generated by Django 4.1.1 on 2022-09-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_name_customuser_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='owner',
            field=models.BooleanField(default=False),
        ),
    ]