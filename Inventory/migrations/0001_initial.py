# Generated by Django 4.2.10 on 2024-02-23 07:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FinishGoods',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FG_name', models.CharField(max_length=50)),
                ('FG_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_name', models.CharField(choices=[('p', 'production'), ('S', 'Sales'), ('U', 'Purchase')], max_length=1)),
                ('Item_name', models.CharField(max_length=55)),
                ('Item_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Purchase_Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('gst_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('company_owner', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RawMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RM_name', models.CharField(max_length=50)),
                ('RM_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales_Party',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('gst_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('company_owner', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='WastageItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('WI_name', models.CharField(max_length=50)),
                ('WI_qty', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Production_Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genrate_date', models.DateTimeField()),
                ('FG', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.finishgoods')),
                ('RM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.rawmaterial')),
                ('WI', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.wastageitem')),
            ],
        ),
    ]
