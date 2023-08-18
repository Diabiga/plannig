# Generated by Django 4.2.4 on 2023-08-18 10:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batiment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Groupe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Heure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Jours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('batiment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.batiment')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.TextField()),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.cycle')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.grade')),
                ('matieres', models.ManyToManyField(related_name='professeurs', to='delta.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Niveau',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('groupes', models.ManyToManyField(related_name='niveaux', to='delta.groupe')),
            ],
        ),
        migrations.AddField(
            model_name='matiere',
            name='niveaux',
            field=models.ManyToManyField(related_name='matieres', to='delta.niveau'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='matieres',
            field=models.ManyToManyField(related_name='groupes', to='delta.matiere'),
        ),
        migrations.AddField(
            model_name='groupe',
            name='niveau',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.niveau'),
        ),
        migrations.CreateModel(
            name='Duree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('matieres', models.ManyToManyField(related_name='durees', to='delta.matiere')),
                ('niveaux', models.ManyToManyField(related_name='durees', to='delta.niveau')),
            ],
        ),
        migrations.AddField(
            model_name='cycle',
            name='professeurs',
            field=models.ManyToManyField(related_name='cycles', to='delta.professeur'),
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.groupe')),
                ('heure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.heure')),
                ('jours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.jours')),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.matiere')),
                ('professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.professeur')),
                ('salle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delta.salle')),
            ],
        ),
    ]