# Generated by Django 3.0.5 on 2021-11-18 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211118_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
