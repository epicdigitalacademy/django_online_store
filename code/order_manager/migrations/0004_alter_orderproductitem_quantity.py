# Generated by Django 4.2.5 on 2023-09-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_manager', '0003_order_items_order_ordered_order_ordered_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproductitem',
            name='quantity',
            field=models.IntegerField(default=1, null=True),
        ),
    ]