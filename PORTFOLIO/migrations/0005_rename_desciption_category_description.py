# Generated by Django 5.0.4 on 2024-04-26 19:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PORTFOLIO', '0004_category_desciption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desciption',
            new_name='description',
        ),
    ]
