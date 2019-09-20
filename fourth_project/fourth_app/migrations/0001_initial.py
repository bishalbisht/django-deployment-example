# Generated by Django 2.2.1 on 2019-09-04 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=260)),
                ('first_name', models.CharField(max_length=160)),
                ('last_name', models.CharField(max_length=160)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
