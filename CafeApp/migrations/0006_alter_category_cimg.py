# Generated by Django 3.2.7 on 2021-09-30 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0005_alter_category_cimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cimg',
            field=models.ImageField(upload_to='picture'),
        ),
    ]
