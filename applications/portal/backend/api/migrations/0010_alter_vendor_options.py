# Generated by Django 4.1.4 on 2023-03-10 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_alter_antibody_target_species_raw"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="vendor",
            options={"ordering": ("name",)},
        ),
    ]
