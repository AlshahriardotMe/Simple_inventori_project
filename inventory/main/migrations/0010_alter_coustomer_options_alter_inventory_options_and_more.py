# Generated by Django 5.0.2 on 2024-03-08 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_coustomer_remove_sell_customer_address_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coustomer',
            options={'verbose_name_plural': '2. Sells'},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name_plural': '7. Inventorys'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': '4. Products'},
        ),
        migrations.AlterModelOptions(
            name='purchace',
            options={'verbose_name_plural': '5. Purchaces'},
        ),
        migrations.AlterModelOptions(
            name='sell',
            options={'verbose_name_plural': '6. Sells'},
        ),
        migrations.AlterModelOptions(
            name='unit',
            options={'verbose_name_plural': '3. Units'},
        ),
    ]