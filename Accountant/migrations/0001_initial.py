# Generated by Django 4.2.10 on 2024-03-28 10:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_genrate', models.DateField(default=django.utils.timezone.now)),
                ('Totall_amt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.sales_party')),
            ],
        ),
        migrations.CreateModel(
            name='sales_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FG_name', models.CharField(max_length=50)),
                ('FG_qty', models.IntegerField()),
                ('FG_price', models.IntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.inventory')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accountant.salesbill')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_genrate', models.DateTimeField()),
                ('Totall_amt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.purchase_party')),
            ],
        ),
        migrations.CreateModel(
            name='purchase_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('RM_name', models.CharField(max_length=50)),
                ('RM_qty', models.IntegerField()),
                ('RM_price', models.IntegerField()),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.inventory')),
                ('purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accountant.purchasebill')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Received',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('sales_party_name', models.CharField(max_length=50)),
                ('paid_date', models.DateField()),
                ('amt_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('sales_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.sales_party')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_paid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('purchase_party_name', models.CharField(max_length=50)),
                ('paid_date', models.DateField()),
                ('amt_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('purchase_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.purchase_party')),
            ],
        ),
        migrations.CreateModel(
            name='MisCExp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_genrate', models.DateTimeField()),
                ('Totall_amt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('P_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.purchase_party')),
                ('S_party', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.sales_party')),
                ('sales_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.finishgoods')),
            ],
        ),
        migrations.CreateModel(
            name='debtors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_amt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('D_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.sales_party')),
                ('sales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accountant.salesbill')),
            ],
        ),
        migrations.CreateModel(
            name='creditors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_amt', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('C_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventory.purchase_party')),
                ('Purchase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accountant.purchasebill')),
            ],
        ),
    ]
