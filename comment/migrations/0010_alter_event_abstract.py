# Generated by Django 4.1.1 on 2022-11-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0009_alter_event_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='abstract',
            field=models.CharField(blank=True, help_text='Write a post excerpt', max_length=100, null=True),
        ),
    ]