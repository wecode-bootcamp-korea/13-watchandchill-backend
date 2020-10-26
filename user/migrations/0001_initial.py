# Generated by Django 3.1.2 on 2020-10-21 07:17

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
                ('email', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=300)),
                ('profile_image_url', models.CharField(max_length=2000)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]