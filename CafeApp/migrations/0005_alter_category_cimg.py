# Generated by Django 3.2.7 on 2021-09-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0004_auto_20210930_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cimg',
            field=models.ImageField(upload_to='Category'),
        ),
    ]
