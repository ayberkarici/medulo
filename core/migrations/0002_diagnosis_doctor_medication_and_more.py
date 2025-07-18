# Generated by Django 5.2.4 on 2025-07-14 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('diploma_no', models.CharField(max_length=20)),
                ('branch', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('barcode', models.CharField(max_length=20)),
                ('dosage', models.CharField(max_length=20)),
                ('period', models.CharField(max_length=20)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='diagnosis',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='doctor_name',
        ),
        migrations.RemoveField(
            model_name='prescription',
            name='medication',
        ),
        migrations.AddField(
            model_name='prescription',
            name='prescription_subtype',
            field=models.CharField(default='Ayaktan', max_length=20),
        ),
        migrations.AddField(
            model_name='prescription',
            name='prescription_type',
            field=models.CharField(default='Normal', max_length=20),
        ),
        migrations.AddField(
            model_name='prescription',
            name='protocol_no',
            field=models.CharField(default='000000', max_length=20),
        ),
        migrations.AddField(
            model_name='prescription',
            name='provision_type',
            field=models.CharField(default='Normal', max_length=20),
        ),
        migrations.AddField(
            model_name='prescription',
            name='remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='report',
            name='report_code',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='prescription',
            name='icd10_codes',
            field=models.ManyToManyField(to='core.diagnosis'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.doctor'),
        ),
        migrations.AddField(
            model_name='prescription',
            name='medications',
            field=models.ManyToManyField(to='core.medication'),
        ),
    ]
