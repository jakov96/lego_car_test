# Generated by Django 3.2.5 on 2021-07-22 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210722_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='widgetconfigurationitem',
            name='widget',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.widget', verbose_name='Виджет'),
        ),
    ]
