# Generated by Django 3.2.5 on 2021-08-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0021_auto_20210810_1214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=200, null=True)),
                ('property_price', models.FloatField(null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(choices=[('Guestroom', 'Guestroom'), ('Display area', 'Dispaly area'), ('Working station', 'Working station'), ('Office', 'Office'), ('Noursing room', 'Noursing room'), ('Food corner', 'Food corner')], max_length=200, null=True)),
                ('building', models.CharField(max_length=200, null=True)),
                ('total_project_price', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]