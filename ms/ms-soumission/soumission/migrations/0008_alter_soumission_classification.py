# Generated by Django 4.0.4 on 2022-06-12 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soumission', '0007_alter_soumission_prix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soumission',
            name='classification',
            field=models.CharField(max_length=50),
        ),
    ]
