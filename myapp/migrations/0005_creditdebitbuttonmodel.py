# Generated by Django 4.0 on 2022-01-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_banktransfermodel_debitmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditDebitButtonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.PositiveBigIntegerField(default=0)),
                ('tag', models.CharField(max_length=200)),
                ('btn_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit'), ('Transfer', 'Transfer')], max_length=20)),
            ],
        ),
    ]
