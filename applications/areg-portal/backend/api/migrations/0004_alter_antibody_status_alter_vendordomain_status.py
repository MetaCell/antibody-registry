# Generated by Django 4.0.6 on 2022-09-12 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_vendor_nif_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='antibody',
            name='status',
            field=models.CharField(choices=[('C', 'CURATED'), ('R', 'REJECTED'), ('Q', 'QUEUE')], default='Q', max_length=1),
        ),
        migrations.AlterField(
            model_name='vendordomain',
            name='status',
            field=models.CharField(choices=[('C', 'CURATED'), ('R', 'REJECTED'), ('Q', 'QUEUE')], default='Q', max_length=1),
        ),
    ]
