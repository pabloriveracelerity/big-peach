# Generated by Django 3.0.4 on 2020-05-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200508_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poststatus',
            name='status',
            field=models.CharField(choices=[('draft', 'draft'), ('published', 'published')], default=('draft', 'draft'), max_length=10),
        ),
    ]
