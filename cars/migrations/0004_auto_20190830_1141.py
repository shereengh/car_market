# Generated by Django 2.1.5 on 2019-08-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_auto_20190827_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
