# Generated by Django 4.1.7 on 2023-04-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='email_address',
            new_name='emailAddress',
        ),
        migrations.AddField(
            model_name='doctor',
            name='mobile',
            field=models.IntegerField(null=True),
        ),
    ]
