# Generated by Django 4.0.6 on 2022-09-23 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='antigen',
            field=models.ForeignKey(db_column='antigen_id', null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.gene'),
        ),
        migrations.AlterField(
            model_name='antibody',
            name='species',
            field=models.ManyToManyField(db_column='target_species', null=True, related_name='targets', through='api.AntibodySpecies', to='api.specie'),
        ),
    ]
