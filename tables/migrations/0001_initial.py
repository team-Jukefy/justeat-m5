# Generated by Django 3.2.16 on 2023-01-12 14:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_number', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('status', models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied')], default='occupied', max_length=9)),
                ('musics_count', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(2), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
