# Generated by Django 5.0.6 on 2024-08-08 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to='accounts.plan'),
        ),
    ]