# Generated by Django 3.2.7 on 2021-09-30 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(max_length=250, unique=True)),
                ('cdes', models.TextField()),
                ('cslug', models.SlugField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('cname',),
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=250, unique=True)),
                ('pslug', models.SlugField(max_length=250, unique=True)),
                ('pimg', models.ImageField(upload_to='')),
                ('pstock', models.IntegerField()),
                ('pavailable', models.BooleanField()),
                ('pprice', models.FloatField()),
                ('pcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CafeApp.category')),
            ],
        ),
    ]
