# Generated by Django 4.0.4 on 2022-05-12 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soumission', '0002_soumission_offre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soumission',
            name='cahierCharge',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='classification',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='delai',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='extraitRole',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='nCnas',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='nbMaterial',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='nbSalarie',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='soumission',
            name='prix',
            field=models.FloatField(null=True),
        ),
    ]
