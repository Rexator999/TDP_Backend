# Generated by Django 5.0.4 on 2024-10-07 05:49

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_rename_most_views_clientrequest_firsthand_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientrequest',
            name='firsthand',
        ),
        migrations.RemoveField(
            model_name='clientrequest',
            name='secondhand',
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='product_con',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
