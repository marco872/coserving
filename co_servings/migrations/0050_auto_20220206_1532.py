# Generated by Django 3.2.5 on 2022-02-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0049_stand'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='temp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='venue',
            name='temp_cost',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]