# Generated by Django 3.1.6 on 2021-02-06 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topping',
            old_name='item',
            new_name='topping',
        ),
    ]