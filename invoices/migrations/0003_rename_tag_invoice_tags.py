# Generated by Django 3.2.16 on 2023-01-10 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0002_auto_20230110_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='tag',
            new_name='tags',
        ),
    ]