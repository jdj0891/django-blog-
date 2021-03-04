# Generated by Django 2.1.5 on 2021-03-04 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0005_auto_20210304_1902'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='text',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogging.Post'),
        ),
    ]
