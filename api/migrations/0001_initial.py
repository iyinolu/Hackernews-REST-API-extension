# Generated by Django 4.1 on 2022-09-25 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storyId', models.IntegerField(unique=True)),
                ('type', models.CharField(choices=[('job', 'Job'), ('story', 'Story'), ('comment', 'Comment'), ('poll', 'Poll'), ('pollopt', 'Poll Option')], max_length=10)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('url', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentId', models.IntegerField(unique=True)),
                ('text', models.CharField(blank=True, max_length=5000, null=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='api.story')),
            ],
        ),
    ]
