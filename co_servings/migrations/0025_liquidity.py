# Generated by Django 3.2.5 on 2021-08-20 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0024_auto_20210819_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liquidity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('price', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('Starting', 'Starting'), ('Filling-up', 'Filling-up'), ('Completed', 'Completed')], max_length=200, null=True)),
            ],
        ),
    ]
