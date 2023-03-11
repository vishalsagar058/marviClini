# Generated by Django 3.2.9 on 2023-03-03 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullName', models.TextField()),
                ('phoneNumber', models.TextField()),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medName', models.TextField()),
                ('currentStock', models.IntegerField()),
                ('lastLoadedStock', models.IntegerField()),
                ('lastLoadingDate', models.DateTimeField(auto_now_add=True)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine_pres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.IntegerField()),
                
                ('customerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cWeb.customer_record')),
                ('medName', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='prescriptions', to='cWeb.medicine_record')),
            ],
        ),
    ]