# Generated by Django 3.2.5 on 2022-01-13 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0043_rename_department_collateral_pool'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fbm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
