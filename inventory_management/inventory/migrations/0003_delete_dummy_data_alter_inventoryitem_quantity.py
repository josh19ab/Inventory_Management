# Generated by Django 4.2.1 on 2023-05-23 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_dummy_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='dummy_data',
        ),
        migrations.AlterField(
            model_name='inventoryitem',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]