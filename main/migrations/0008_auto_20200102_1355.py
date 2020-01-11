# Generated by Django 3.0.1 on 2020-01-02 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_blogarticle_associate_with'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogarticle',
            name='associate_with',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.SiteArticle'),
        ),
    ]
