# Generated by Django 3.2.16 on 2023-01-09 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hra', '0003_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='description'),
        ),
    ]
