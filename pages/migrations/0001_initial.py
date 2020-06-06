# Generated by Django 3.0.7 on 2020-06-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=10)),
                ('lastname', models.CharField(max_length=10)),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='matchmaking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matchname', models.CharField(max_length=20)),
                ('datetoplay', models.DateTimeField()),
                ('city', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('match_id', models.IntegerField()),
                ('user_id', models.ManyToManyField(to='pages.users')),
            ],
        ),
    ]