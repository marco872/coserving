# Generated by Django 3.2.5 on 2021-07-23 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('co_servings', '0004_investment'),
    ]

    operations = [
        migrations.AddField(
            model_name='investment',
            name='webinvestor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='co_servings.webinvestor'),
        ),
    ]