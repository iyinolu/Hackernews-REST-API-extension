# Generated by Django 4.1 on 2022-09-25 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]