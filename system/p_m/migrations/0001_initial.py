# Generated by Django 3.2.2 on 2021-06-11 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulli', models.CharField(choices=[('Financa', 'Financa'), ('Sekretaria', 'Sekretaria'), ('Administrata', 'Administrata'), ('IT', 'IT'), ('HR', 'HR'), ('Marketingu', 'Marketingu'), ('Shitjet', 'Shitjet')], max_length=100)),
                ('parent_departament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='p_m.departament')),
            ],
        ),
        migrations.CreateModel(
            name='DitePushimi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('emri_i_festes', models.CharField(max_length=200)),
                ('statusi', models.CharField(choices=[('Aktive', 'Aktive'), ('Joaktive', 'Joaktive')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Pozicionet',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False)),
                ('pozicioni', models.CharField(choices=[('HR', 'HR'), ('Pergjegjes Departamenti', 'Pergjegjes Departamenti'), ('Punonjes Departamenti', 'Punonjes Departamenti')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Punonjes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emer', models.CharField(max_length=100)),
                ('mbiemer', models.CharField(max_length=100)),
                ('data_e_fillimit', models.DateField(null=True)),
                ('data_e_mbarimit', models.DateField(null=True)),
                ('gjinia', models.CharField(choices=[('Femer', 'Femer'), ('Mashkull', 'Mashkull')], max_length=100)),
                ('numri_i_telefonit', models.CharField(max_length=10, null=True)),
                ('statusi', models.CharField(choices=[('Aktiv', 'Aktiv'), ('Joaktiv', 'Joaktiv')], max_length=100)),
                ('departamenti', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p_m.departament')),
                ('pozicioni', models.ManyToManyField(to='p_m.Pozicionet')),
                ('username', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lejet',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('data_e_kerkeses', models.DateTimeField(auto_now_add=True)),
                ('lloji_i_lejes', models.CharField(choices=[('Leje e paguar', 'Leje e paguar'), ('Leje e papaguar', 'Leje e papaguar')], max_length=100)),
                ('fillimi', models.DateTimeField()),
                ('mbarimi', models.DateTimeField()),
                ('statusi', models.CharField(choices=[('Ne pritje', 'Ne pritje'), ('Pranuar', 'Pranuar'), ('Anulluar', 'Anulluar')], max_length=100)),
                ('arsyetimi', models.TextField()),
                ('punonjes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_m.punonjes')),
            ],
            options={
                'ordering': ['data_e_kerkeses'],
            },
        ),
        migrations.CreateModel(
            name='Departament_per_punonjes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='p_m.departament')),
                ('punonjes', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='p_m.punonjes')),
            ],
        ),
        migrations.AddField(
            model_name='departament',
            name='pergjegjesi',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p_m.punonjes'),
        ),
    ]
