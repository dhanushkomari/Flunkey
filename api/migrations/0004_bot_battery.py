# Generated by Django 3.1.4 on 2021-11-16 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_finaldelivery_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='battery',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
