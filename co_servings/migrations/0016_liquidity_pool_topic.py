# Generated by Django 3.2.5 on 2021-08-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0015_auto_20210802_0942'),
    ]

    operations = [
        migrations.AddField(
            model_name='liquidity_pool',
            name='topic',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
