# Generated by Django 4.0.4 on 2022-05-28 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EVENTS', '0002_alter_eveniment_template_an_incepere_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eveniment',
            name='data_finalizare',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='eveniment',
            name='status',
            field=models.BooleanField(),
        ),
    ]
