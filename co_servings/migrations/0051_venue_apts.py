# Generated by Django 3.2.5 on 2022-02-06 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0050_auto_20220206_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='apts',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]