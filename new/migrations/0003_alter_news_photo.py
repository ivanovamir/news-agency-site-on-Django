# Generated by Django 4.0.3 on 2022-05-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_alter_tag_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(null=True, upload_to='new/%Y/%m/%d/'),
        ),
    ]
