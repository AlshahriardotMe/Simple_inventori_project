# Generated by Django 5.0.2 on 2024-02-18 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_purchace'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('sell_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(blank=True, max_length=50)),
                ('customer_mobile', models.CharField(max_length=20)),
                ('customer_address', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
            ],
            options={
                'verbose_name_plural': 'Sells',
            },
        ),
    ]