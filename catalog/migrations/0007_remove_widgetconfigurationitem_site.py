# Generated by Django 3.2.5 on 2021-07-22 11:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_widgetconfigurationitem_site'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='widgetconfigurationitem',
            name='site',
        ),
    ]