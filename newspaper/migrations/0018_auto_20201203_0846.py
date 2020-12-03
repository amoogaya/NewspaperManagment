# Generated by Django 3.1.3 on 2020-12-03 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0017_auto_20201203_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='text_ar',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
