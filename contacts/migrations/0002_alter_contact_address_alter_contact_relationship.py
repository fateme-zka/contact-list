# Generated by Django 4.0.5 on 2022-06-14 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='relationship',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]