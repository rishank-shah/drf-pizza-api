# Generated by Django 3.1.6 on 2021-02-07 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20210207_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizzasize',
            old_name='size',
            new_name='pizza_size',
        ),
    ]
