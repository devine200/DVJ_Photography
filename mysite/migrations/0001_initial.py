# Generated by Django 2.2 on 2020-06-12 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('booking_id', models.CharField(max_length=10)),
            ],
        ),
    ]
