# Generated by Django 4.0.6 on 2022-09-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_antibody_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='product_isotype',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
