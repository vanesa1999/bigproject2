# Generated by Django 3.2.2 on 2021-05-10 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstpart', '0004_lejet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balanca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lloji_i_lejes', models.CharField(choices=[('Leje e paguar', 'Leje e paguar'), ('Leje e papaguar', 'Leje e papaguar')], max_length=100)),
                ('nga', models.DateTimeField()),
                ('ne', models.DateTimeField()),
                ('totali_i_oreve_te_perdorshme', models.PositiveIntegerField(default=0)),
                ('totali_i_lejeve_te_marra', models.PositiveIntegerField(default=0)),
                ('punonjes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='firstpart.punonjes')),
            ],
        ),
    ]
