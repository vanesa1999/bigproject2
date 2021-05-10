# Generated by Django 3.2.2 on 2021-05-10 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstpart', '0003_dite_pushimi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lejet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_e_kerkeses', models.DateTimeField(auto_now_add=True)),
                ('lloji_i_lejes', models.CharField(choices=[('Leje e paguar', 'Leje e paguar'), ('Leje e papaguar', 'Leje e papaguar')], max_length=100)),
                ('fillimi', models.DateTimeField()),
                ('mbarimi', models.DateTimeField()),
                ('statusi', models.CharField(choices=[('Ne pritje', 'Ne pritje'), ('Pranuar', 'Pranuar'), ('Anulluar', 'Anulluar')], default='Ne pritje', max_length=100)),
                ('arsyetimi', models.TextField()),
                ('punonjes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='firstpart.punonjes')),
            ],
            options={
                'ordering': ['data_e_kerkeses'],
            },
        ),
    ]
