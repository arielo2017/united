# Generated by Django 3.0.7 on 2020-06-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200606_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='training',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_name', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('date', models.DateTimeField()),
                ('training_id', models.IntegerField()),
                ('user_id', models.ManyToManyField(to='pages.users')),
            ],
        ),
    ]
