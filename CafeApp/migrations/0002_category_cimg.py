# Generated by Django 3.2.7 on 2021-09-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CafeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='cimg',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]
