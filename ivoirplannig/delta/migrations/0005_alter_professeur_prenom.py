# Generated by Django 4.2.4 on 2023-08-20 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delta', '0004_remove_professeur_cycle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professeur',
            name='prenom',
            field=models.CharField(max_length=100),
        ),
    ]
