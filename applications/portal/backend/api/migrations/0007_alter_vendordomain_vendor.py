# Generated by Django 4.1.4 on 2023-02-10 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0006_alter_antibody_antigen_alter_antibody_vendor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vendordomain",
            name="vendor",
            field=models.ForeignKey(
                db_column="vendor_id",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="api.vendor",
            ),
        ),
    ]
