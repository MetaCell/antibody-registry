# Generated by Django 4.0.6 on 2022-09-12 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_antibody_commercial_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='nif_id',
            field=models.CharField(db_column='nif_id', max_length=32),
        ),
    ]
