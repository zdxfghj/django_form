# Generated by Django 4.2.11 on 2024-05-09 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_alter_artiles_info_alter_artiles_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiles',
            name='service_type',
            field=models.CharField(choices=[('Ride hailing', 'Ride hailing'), ('Taxi', 'Taxi'), ('Executive cars', 'Executive cars'), ('Aiport shuttle', 'Aiport shuttle'), ('Bikes or motorbikes', 'Bikes or motorbikes'), ('Delivery', 'Delivery'), ('Other', 'Other')], default='Other', max_length=20),
        ),
    ]
