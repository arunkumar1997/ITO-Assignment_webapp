# Generated by Django 3.1.1 on 2020-09-12 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Company', models.CharField(max_length=100)),
                ('Model', models.CharField(max_length=100)),
                ('Color', models.CharField(max_length=100)),
                ('Date', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('Engine_capacity', models.CharField(max_length=100)),
                ('Number_plate', models.CharField(max_length=100)),
                ('Seating_capacity', models.CharField(max_length=10)),
            ],
        ),
    ]