# Generated by Django 4.0.6 on 2022-09-20 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_antibody_subregion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='modifications',
            field=models.CharField(db_column='target_modification', max_length=64, null=True),
        ),
    ]
