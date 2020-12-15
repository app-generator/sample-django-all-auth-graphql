# Generated by Django 2.1.15 on 2020-12-15 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_for', models.CharField(max_length=100)),
                ('issue_date', models.DateField()),
                ('due_date', models.DateField()),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(max_length=10)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'transaction',
                'verbose_name_plural': 'transactions',
            },
        ),
    ]
