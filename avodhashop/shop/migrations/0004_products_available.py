# Generated by Django 2.2 on 2022-06-29 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20220627_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='available',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]