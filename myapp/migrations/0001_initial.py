# Generated by Django 4.0 on 2022-01-06 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CreditModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amt', models.PositiveBigIntegerField(default=0)),
                ('tag', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
