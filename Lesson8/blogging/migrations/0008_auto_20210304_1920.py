# Generated by Django 2.1.5 on 2021-03-04 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0007_auto_20210304_1919'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_on']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='created_date',
            new_name='created_on',
        ),
    ]
