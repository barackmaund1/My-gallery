# Generated by Django 2.2.10 on 2020-05-24 08:59

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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(max_length=50)),
                ('image_description', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='images/')),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('image_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Category')),
                ('image_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='photos.Location')),
            ],
        ),
    ]