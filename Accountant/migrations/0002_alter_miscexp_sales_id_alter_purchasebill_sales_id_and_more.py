# Generated by Django 4.2.10 on 2024-03-15 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0001_initial'),
        ('Accountant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miscexp',
            name='sales_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.finishgoods'),
        ),
        migrations.AlterField(
            model_name='purchasebill',
            name='sales_ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rawmaterial'),
        ),
        migrations.AlterField(
            model_name='salesbill',
            name='sales_Id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.finishgoods'),
        ),
        migrations.DeleteModel(
            name='SalesItem',
        ),
    ]
