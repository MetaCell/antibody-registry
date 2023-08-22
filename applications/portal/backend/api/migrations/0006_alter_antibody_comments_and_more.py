# Generated by Django 4.1.4 on 2023-08-22 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0005_alter_vendordomain_base_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="antibody",
            name="comments",
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="antibody",
            name="commercial_type",
            field=models.CharField(
                blank=True,
                choices=[
                    ("commercial", "commercial"),
                    ("personal", "personal"),
                    ("non-profit", "non-profit"),
                    ("other", "other"),
                ],
                db_index=True,
                default="other",
                max_length=32,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="antibody",
            name="defining_citation",
            field=models.CharField(
                blank=True, db_index=True, max_length=16384, null=True
            ),
        ),
        migrations.AlterField(
            model_name="antibody",
            name="show_link",
            field=models.BooleanField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="antibody",
            name="target_species_raw",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="Comma separated value for target species. Values filled here will be parsed and assigned to the 'Target species' field.",
                max_length=4096,
                null=True,
                verbose_name="Target species (csv)",
            ),
        ),
        migrations.AlterField(
            model_name="application",
            name="name",
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name="specie",
            name="name",
            field=models.CharField(db_index=True, max_length=4096, unique=True),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="commercial_type",
            field=models.CharField(
                choices=[
                    ("commercial", "commercial"),
                    ("personal", "personal"),
                    ("non-profit", "non-profit"),
                    ("other", "other"),
                ],
                db_index=True,
                default="other",
                max_length=32,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="show_link",
            field=models.BooleanField(
                blank=True, db_index=True, default=False, null=True
            ),
        ),
    ]
