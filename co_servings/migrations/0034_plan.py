# Generated by Django 3.2.5 on 2021-10-15 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0033_auto_20211007_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
