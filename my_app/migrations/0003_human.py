# Generated by Django 4.0.1 on 2022-01-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Human',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
