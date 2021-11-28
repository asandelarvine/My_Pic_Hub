# Generated by Django 3.2.9 on 2021-11-25 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_pic_hub', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.CharField(max_length=30, null=True)),
                ('image_description', models.CharField(max_length=3000)),
                ('categories', models.ManyToManyField(to='my_pic_hub.Category')),
            ],
        ),
    ]
