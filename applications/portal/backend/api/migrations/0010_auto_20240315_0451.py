# Generated by Django 4.2.10 on 2024-02-20 12:51

import api.models
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ("api", "0009_auto_20240220_0451"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DROP MATERIALIZED VIEW IF EXISTS antibody_search;
            CREATE MATERIALIZED VIEW antibody_search AS 
            SELECT ix, 
            (
                setweight(to_tsvector('english'::regconfig, (((
                COALESCE(ab_name, ''::text) || ' '::text) || 
                        COALESCE(clone_id, ''::text) || ' '::text)) 
            ), 'A'::"char") ||
                
                setweight(to_tsvector('english'::regconfig, (((((((((((((((((((((((((
                    COALESCE(api_vendor.vendor, ''::text) || ' '::text) || 
                    COALESCE(api_specie.name, ''::text) || ' '::text) || 
                    COALESCE(target_subregion, ''::text) || ' '::text) || 
                        COALESCE(clonality, ''::text)) || ' '::text) || 
                    COALESCE(target_modification, ''::text)) || ' '::text) || 
                    COALESCE(epitope, ''::character varying)::text) || ' '::text) || 
                    COALESCE(product_isotype, ''::character varying)::text) || ' '::text) || 
					COALESCE(ab_target, ''::character varying)::text) || ' '::text) ||
					COALESCE(ab_target_entrez_gid, ''::character varying)::text) || ' '::text) ||
					COALESCE(uniprot_id, ''::character varying)::text) || ' '::text) ||
					COALESCE(product_isotype, ''::character varying)::text) || ' '::text) ||
                COALESCE(product_conjugate, ''::text) || 
                COALESCE(product_form, ''::character varying)::text) || ' '::text) || 
                COALESCE(target_species_raw, ''::character varying)::text) || ' '::text) || 
                COALESCE(kit_contents, ''::character varying)::text) || ' '::text)), 'C'::"char") ||
            setweight(to_tsvector('english'::regconfig, (((
                COALESCE(comments, ''::text) || ' '::text) || 
                        COALESCE(curator_comment, ''::text) || ' '::text)) 
            ), 'D'::"char")

            ) AS search_vector,
            CASE 
                WHEN api_antibody.defining_citation ~ '^([0-9]+[.])?[0-9]+$' THEN CAST(api_antibody.defining_citation AS FLOAT)
                ELSE 0
            END as citations,
            CASE 
                WHEN api_antibody.catalog_num_search ~ '^([0-9]+[.])?[0-9]+$' THEN CAST(api_antibody.catalog_num_search AS FLOAT)
                ELSE 0
            END as catalog_number_search,
            CASE 
                WHEN disc_date IS NOT NULL THEN 1
                ELSE 0
            END AS disc,
            status
            FROM api_antibody 
            LEFT JOIN api_vendor ON api_vendor.id = api_antibody.vendor_id
            LEFT JOIN api_specie ON api_specie.id = api_antibody.source_organism_id
            """,
            reverse_sql="""
            DROP MATERIALIZED VIEW antibody_search;
            """,
        ),
        migrations.RunSQL(
            sql="""CREATE UNIQUE INDEX IF NOT EXISTS antibody_search_idx
                    ON antibody_search
                    (ix);
                    """,
        ),
        migrations.AddIndex(
            model_name="antibodysearch",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["search_vector"], name="antibody_search_fts_idx"
            ),
        ),
    ]
