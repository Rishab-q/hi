# Generated by Django 5.0.3 on 2024-03-19 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0009_alter_inventory_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.CreateModel(
            name='Vendor_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('threshold', models.IntegerField()),
                ('book', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bookstore.book')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookstore.vendor')),
            ],
        ),
    ]