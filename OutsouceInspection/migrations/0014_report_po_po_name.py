# Generated by Django 4.0 on 2023-04-15 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OutsouceInspection', '0013_product_arrival_qty_product_arrival_total_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_po',
            name='po_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]