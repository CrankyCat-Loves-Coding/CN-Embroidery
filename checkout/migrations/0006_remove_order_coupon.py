# Generated by Django 4.1.1 on 2022-09-25 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_coupon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='coupon',
        ),
    ]