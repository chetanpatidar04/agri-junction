# Generated by Django 4.1 on 2022-08-29 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('mob_number', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=500)),
                ('city', models.CharField(default='Shajapur', max_length=50)),
                ('state', models.CharField(default='Madhya Pradesh', max_length=50)),
                ('pincode', models.IntegerField(max_length=6)),
            ],
        ),
    ]
