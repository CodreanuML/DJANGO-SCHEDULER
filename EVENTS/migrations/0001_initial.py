# Generated by Django 4.0.4 on 2022-05-24 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PROJECTS', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Eveniment_Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('activitati_necesare', models.TextField(max_length=300)),
                ('recurenenta', models.CharField(choices=[('saptamanal -7 zile', 'saptamanal'), ('lunar - 28 zile', 'lunar'), ('anual -12 luni * 28 zile', 'anual'), ('2ani =24 luni *28 zile', '2ani')], max_length=100)),
                ('recurenenta_zile', models.IntegerField()),
                ('zile_executie', models.IntegerField()),
                ('an_incepere', models.IntegerField(choices=[('2022', 2022), ('2023', 2023), ('2024', 2024), ('2025', 2025), ('2026', 2026)], max_length=100)),
                ('luna_incepere', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12)], max_length=100)),
                ('zi_incepere', models.IntegerField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('11', 11), ('12', 12), ('13', 13), ('14', 14), ('15', 15), ('16', 16), ('17', 17), ('18', 18), ('19', 19), ('20', 20), ('21', 21), ('22', 22), ('23', 23), ('24', 24), ('25', 25), ('26', 26), ('27', 27), ('28', 28)], max_length=100)),
                ('data_initiere', models.DateField(null=True)),
                ('status', models.BooleanField()),
                ('proiect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evenimente', to='PROJECTS.proiect')),
            ],
        ),
        migrations.CreateModel(
            name='Eveniment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_initiere', models.DateField()),
                ('data_finalizare', models.DateField(null=True)),
                ('status', models.IntegerField()),
                ('eveniment_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eveniment_obj', to='EVENTS.eveniment_template')),
                ('responsabil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eveniment_inst', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['data_finalizare'],
            },
        ),
    ]
