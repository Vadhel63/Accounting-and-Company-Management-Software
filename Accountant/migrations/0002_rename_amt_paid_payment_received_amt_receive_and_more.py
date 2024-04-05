# Generated by Django 4.2.11 on 2024-04-04 16:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Accountant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment_received',
            old_name='amt_paid',
            new_name='amt_receive',
        ),
        migrations.RenameField(
            model_name='payment_received',
            old_name='date',
            new_name='receive_date',
        ),
        migrations.RemoveField(
            model_name='miscexp',
            name='P_party',
        ),
        migrations.RemoveField(
            model_name='miscexp',
            name='S_party',
        ),
        migrations.RemoveField(
            model_name='miscexp',
            name='sales_Id',
        ),
        migrations.RemoveField(
            model_name='payment_paid',
            name='date',
        ),
        migrations.RemoveField(
            model_name='payment_paid',
            name='purchase_party_name',
        ),
        migrations.RemoveField(
            model_name='payment_received',
            name='paid_date',
        ),
        migrations.RemoveField(
            model_name='payment_received',
            name='sales_party_name',
        ),
        migrations.RemoveField(
            model_name='purchase_item',
            name='inventory',
        ),
        migrations.RemoveField(
            model_name='sales_item',
            name='inventory',
        ),
        migrations.AddField(
            model_name='miscexp',
            name='expense_title',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AlterField(
            model_name='payment_paid',
            name='paid_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name='MisCExp_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expense_name', models.CharField(max_length=50)),
                ('expense_qty', models.IntegerField()),
                ('expense_price', models.IntegerField()),
                ('expense', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accountant.miscexp')),
            ],
        ),
    ]
