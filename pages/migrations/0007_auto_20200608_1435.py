# Generated by Django 3.0.7 on 2020-06-08 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20200608_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='Date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='training',
            name='form_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]