# Generated by Django 3.1.2 on 2020-10-29 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newspaper', '0002_auto_20201029_1712'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
                ('Category', models.CharField(choices=[('spor', 'sport'), ('history', 'historical'), ('tourism', 'tourism')], max_length=10)),
                ('body', models.TextField(default='')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newspaper.authors')),
            ],
        ),
    ]
