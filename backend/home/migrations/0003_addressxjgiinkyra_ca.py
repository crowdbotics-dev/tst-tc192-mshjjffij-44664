# Generated by Django 2.2.28 on 2022-11-16 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addressxjgiinkyra'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressxjgiinkyra',
            name='ca',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
