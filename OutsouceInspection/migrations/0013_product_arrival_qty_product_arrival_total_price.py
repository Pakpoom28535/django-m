# Generated by Django 4.0 on 2023-04-15 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OutsouceInspection', '0012_custormer_report_po_product_arrival'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_arrival',
            name='qty',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product_arrival',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]