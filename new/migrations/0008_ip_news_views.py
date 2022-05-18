# Generated by Django 4.0.3 on 2022-05-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0007_alter_tag_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'ip',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.ManyToManyField(blank=True, related_name='post_views', to='new.ip'),
        ),
    ]