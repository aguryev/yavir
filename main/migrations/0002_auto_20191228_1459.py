# Generated by Django 3.0.1 on 2019-12-28 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitearticle',
            old_name='index',
            new_name='position',
        ),
    ]
