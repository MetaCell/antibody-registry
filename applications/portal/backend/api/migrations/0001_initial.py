# Generated by Django 4.1.4 on 2022-12-23 15:53

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions
import django.db.models.functions.comparison
import django.db.models.functions.text


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Antibody",
            fields=[
                (
                    "ix",
                    models.AutoField(primary_key=True, serialize=False, unique=True),
                ),
                ("ab_name", models.CharField(db_index=True, max_length=512, null=True)),
                ("ab_id", models.CharField(db_index=True, max_length=32, null=True)),
                ("accession", models.CharField(blank=True, max_length=32, null=True)),
                (
                    "commercial_type",
                    models.CharField(
                        choices=[
                            ("commercial", "commercial"),
                            ("personal", "personal"),
                            ("non-profit", "non-profit"),
                            ("other", "other"),
                        ],
                        default="other",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "uid",
                    models.CharField(
                        blank=True, db_index=True, max_length=256, null=True
                    ),
                ),
                ("uid_legacy", models.IntegerField(blank=True, null=True)),
                (
                    "catalog_num",
                    models.CharField(db_index=True, max_length=256, null=True),
                ),
                (
                    "cat_alt",
                    models.CharField(
                        blank=True, db_index=True, max_length=512, null=True
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        blank=True, db_index=True, max_length=2048, null=True
                    ),
                ),
                (
                    "target_species_raw",
                    models.CharField(db_index=True, max_length=4096, null=True),
                ),
                (
                    "subregion",
                    models.CharField(
                        blank=True,
                        db_column="target_subregion",
                        db_index=True,
                        max_length=256,
                        null=True,
                    ),
                ),
                (
                    "modifications",
                    models.CharField(
                        blank=True,
                        db_column="target_modification",
                        db_index=True,
                        max_length=128,
                        null=True,
                    ),
                ),
                (
                    "epitope",
                    models.CharField(
                        blank=True, db_index=True, max_length=1024, null=True
                    ),
                ),
                (
                    "clonality",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("unknown", "Unknown"),
                            ("cocktail", "Cocktail"),
                            ("control", "Control"),
                            ("isotype control", "Isotype Control"),
                            ("monoclonal", "Monoclonal"),
                            ("monoclonal secondary", "Monoclonal Secondary"),
                            ("polyclonal", "Polyclonal"),
                            ("polyclonal secondary", "Polyclonal Secondary"),
                            ("oligoclonal", "Oligoclonal"),
                            ("recombinant", "Recombinant"),
                            ("recombinant monoclonal", "Recombinant Monoclonal"),
                            (
                                "recombinant monoclonal secondary",
                                "Recombinant Monoclonal Secondary",
                            ),
                            ("recombinant polyclonal", "Recombinant Polyclonal"),
                            (
                                "recombinant polyclonal secondary",
                                "Recombinant Polyclonal Secondary",
                            ),
                        ],
                        db_index=True,
                        default="unknown",
                        max_length=32,
                        null=True,
                    ),
                ),
                (
                    "clone_id",
                    models.CharField(
                        blank=True, db_index=True, max_length=256, null=True
                    ),
                ),
                (
                    "product_isotype",
                    models.CharField(
                        blank=True, db_index=True, max_length=256, null=True
                    ),
                ),
                (
                    "product_conjugate",
                    models.CharField(
                        blank=True, db_index=True, max_length=512, null=True
                    ),
                ),
                (
                    "defining_citation",
                    models.CharField(
                        blank=True, db_index=True, max_length=16384, null=True
                    ),
                ),
                (
                    "product_form",
                    models.CharField(
                        blank=True, db_index=True, max_length=1024, null=True
                    ),
                ),
                ("comments", models.TextField(blank=True, null=True)),
                (
                    "kit_contents",
                    models.TextField(blank=True, db_index=True, null=True),
                ),
                ("feedback", models.TextField(blank=True, db_index=True, null=True)),
                (
                    "curator_comment",
                    models.TextField(blank=True, db_index=True, null=True),
                ),
                (
                    "disc_date",
                    models.CharField(
                        blank=True, db_index=True, max_length=128, null=True
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CURATED", "Curated"),
                            ("REJECTED", "Rejected"),
                            ("QUEUE", "Queued"),
                        ],
                        db_index=True,
                        default="QUEUE",
                        max_length=8,
                    ),
                ),
                (
                    "insert_time",
                    models.DateTimeField(auto_now_add=True, db_index=True, null=True),
                ),
                (
                    "lastedit_time",
                    models.DateTimeField(auto_now=True, db_index=True, null=True),
                ),
                (
                    "curate_time",
                    models.DateTimeField(blank=True, db_index=True, null=True),
                ),
            ],
            options={
                "verbose_name_plural": "antibodies",
            },
        ),
        migrations.CreateModel(
            name="AntibodyApplications",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AntibodySpecies",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Antigen",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "symbol",
                    models.CharField(
                        db_column="ab_target", db_index=True, max_length=1024, null=True
                    ),
                ),
                (
                    "entrez_id",
                    models.CharField(
                        blank=True,
                        db_column="ab_target_entrez_gid",
                        db_index=True,
                        max_length=2048,
                        null=True,
                    ),
                ),
                (
                    "uniprot_id",
                    models.CharField(
                        blank=True, db_index=True, max_length=64, null=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Specie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=4096, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Vendor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(db_column="vendor", db_index=True, max_length=512),
                ),
                (
                    "nif_id",
                    models.CharField(
                        blank=True, db_column="nif_id", max_length=32, null=True
                    ),
                ),
                (
                    "eu_id",
                    models.CharField(
                        blank=True, db_column="euid", max_length=255, null=True
                    ),
                ),
                (
                    "commercial_type",
                    models.CharField(
                        choices=[
                            ("commercial", "commercial"),
                            ("personal", "personal"),
                            ("non-profit", "non-profit"),
                            ("other", "other"),
                        ],
                        default="other",
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VendorSynonym",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(db_index=True, max_length=512)),
                (
                    "vendor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.vendor"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VendorDomain",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "base_url",
                    models.URLField(
                        db_column="domain_name",
                        db_index=True,
                        max_length=2048,
                        null=True,
                        unique=True,
                    ),
                ),
                (
                    "is_domain_visible",
                    models.BooleanField(db_column="link", default=True),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("CURATED", "Curated"),
                            ("REJECTED", "Rejected"),
                            ("QUEUE", "Queued"),
                        ],
                        db_index=True,
                        default="QUEUE",
                        max_length=8,
                    ),
                ),
                (
                    "vendor",
                    models.ForeignKey(
                        db_column="vendor_id",
                        null=True,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="api.vendor",
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="vendor",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector("name", config="english"),
                name="vendor_name_fts_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="antigen",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector("symbol", config="english"),
                name="gene_symbol_fts_idx",
            ),
        ),
        migrations.AddField(
            model_name="antibodyspecies",
            name="antibody",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.antibody"
            ),
        ),
        migrations.AddField(
            model_name="antibodyspecies",
            name="specie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.specie"
            ),
        ),
        migrations.AddField(
            model_name="antibodyapplications",
            name="antibody",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.antibody"
            ),
        ),
        migrations.AddField(
            model_name="antibodyapplications",
            name="application",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.application"
            ),
        ),
        migrations.AddField(
            model_name="antibody",
            name="antigen",
            field=models.ForeignKey(
                db_column="antigen_id",
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                to="api.antigen",
            ),
        ),
        migrations.AddField(
            model_name="antibody",
            name="applications",
            field=models.ManyToManyField(
                blank=True, through="api.AntibodyApplications", to="api.application"
            ),
        ),
        migrations.AddField(
            model_name="antibody",
            name="source_organism",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="source",
                to="api.specie",
            ),
        ),
        migrations.AddField(
            model_name="antibody",
            name="species",
            field=models.ManyToManyField(
                blank=True,
                db_column="target_species",
                related_name="targets",
                through="api.AntibodySpecies",
                to="api.specie",
            ),
        ),
        migrations.AddField(
            model_name="antibody",
            name="vendor",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.RESTRICT, to="api.vendor"
            ),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector(
                    "catalog_num__normalize",
                    "cat_alt__normalize_relaxed",
                    config="english",
                ),
                name="antibody_catalog_num_fts_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=models.Index(
                models.OrderBy(
                    django.db.models.expressions.CombinedExpression(
                        django.db.models.functions.text.Length(
                            django.db.models.functions.comparison.Coalesce(
                                "defining_citation", models.Value("")
                            )
                        ),
                        "-",
                        django.db.models.functions.text.Length(
                            django.db.models.functions.comparison.Coalesce(
                                "defining_citation__remove_coma", models.Value("")
                            )
                        ),
                    ),
                    descending=True,
                ),
                name="antibody_nb_citations_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=models.Index(
                models.OrderBy(
                    django.db.models.expressions.CombinedExpression(
                        django.db.models.expressions.CombinedExpression(
                            django.db.models.functions.text.Length(
                                django.db.models.functions.comparison.Coalesce(
                                    "defining_citation", models.Value("")
                                )
                            ),
                            "-",
                            django.db.models.functions.text.Length(
                                django.db.models.functions.comparison.Coalesce(
                                    "defining_citation__remove_coma", models.Value("")
                                )
                            ),
                        ),
                        "-",
                        django.db.models.expressions.CombinedExpression(
                            models.Value(100),
                            "+",
                            django.db.models.functions.text.Length(
                                django.db.models.functions.comparison.Coalesce(
                                    "disc_date", models.Value("")
                                )
                            ),
                        ),
                    ),
                    descending=True,
                ),
                name="antibody_nb_citations_idx2",
            ),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=models.Index(fields=["-disc_date"], name="antibody_discontinued_idx"),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector(
                    "ab_name",
                    "clone_id__normalize_relaxed",
                    config="english",
                    weight="A",
                ),
                name="antibody_name_fts_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.CombinedSearchVector(
                    django.contrib.postgres.search.SearchVector(
                        "ab_name",
                        "clone_id__normalize_relaxed",
                        config="english",
                        weight="A",
                    ),
                    "||",
                    django.contrib.postgres.search.SearchVector(
                        "accession",
                        "commercial_type",
                        "uid",
                        "uid_legacy",
                        "url",
                        "subregion",
                        "modifications",
                        "epitope",
                        "clonality",
                        "product_isotype",
                        "product_conjugate",
                        "defining_citation",
                        "product_form",
                        "comments",
                        "kit_contents",
                        "feedback",
                        "curator_comment",
                        "disc_date",
                        "status",
                        config="english",
                        weight="C",
                    ),
                    django.contrib.postgres.search.SearchConfig("english"),
                ),
                name="antibody_all_fts_idx",
            ),
        ),
        migrations.AddIndex(
            model_name="antibody",
            index=django.contrib.postgres.indexes.GinIndex(
                django.contrib.postgres.search.SearchVector(
                    "accession",
                    "commercial_type",
                    "uid",
                    "uid_legacy",
                    "url",
                    "subregion",
                    "modifications",
                    "epitope",
                    "clonality",
                    "product_isotype",
                    "product_conjugate",
                    "defining_citation",
                    "product_form",
                    "comments",
                    "kit_contents",
                    "feedback",
                    "curator_comment",
                    "disc_date",
                    "status",
                    config="english",
                    weight="C",
                ),
                name="antibody_all_fts_idx2",
            ),
        ),
        migrations.AddConstraint(
            model_name="antibody",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(("status", "curated"), _negated=True),
                    models.Q(
                        ("status", "curated"),
                        ("catalog_num__isnull", False),
                        ("ab_name__isnull", False),
                        ("ab_name__exact", ""),
                        ("vendor__isnull", False),
                    ),
                    _connector="OR",
                ),
                name="curated_constraints",
            ),
        ),
    ]
