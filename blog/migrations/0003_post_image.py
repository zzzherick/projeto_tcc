# Generated by Django 3.0.6 on 2020-08-31 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200817_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.CharField(default=1, max_length=999),
            preserve_default=False,
        ),
    ]