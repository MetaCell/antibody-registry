# Generated by Django 4.0.6 on 2022-09-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_antibody_ab_id_alter_antibody_accession_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='disc_date',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
