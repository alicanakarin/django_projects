# Generated by Django 3.0.4 on 2020-03-07 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 't_basic_unit',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('phone', models.CharField(blank=True, max_length=60)),
                ('email', models.CharField(blank=True, max_length=60)),
                ('address', models.TextField()),
            ],
            options={
                'db_table': 't_supplier',
            },
        ),
        migrations.CreateModel(
            name='MaterialStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_active', models.BooleanField(default=False)),
                ('stock_name', models.CharField(blank=True, max_length=140, null=True)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('basic_unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stok.BasicUnit')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stok.Currency')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stok.Supplier')),
            ],
            options={
                'db_table': 't_material_stock',
            },
        ),
    ]
