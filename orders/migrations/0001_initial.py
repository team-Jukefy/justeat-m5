# Generated by Django 3.2.16 on 2023-01-12 14:52

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinValueValidator(1)])),
                ('payment', models.CharField(choices=[('pending', 'Pending'), ('paid', 'Paid')], default='pending', max_length=7)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_orders', to='menu.menu')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
