# Generated by Django 3.2.7 on 2021-09-28 12:23

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('elsys', '0002_alter_car_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=50),
        ),
    ]