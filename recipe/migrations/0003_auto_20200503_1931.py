# Generated by Django 3.0.5 on 2020-05-03 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_auto_20200503_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeitem',
            old_name='procedure',
            new_name='instructions',
        ),
    ]
