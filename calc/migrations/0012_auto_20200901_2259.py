# Generated by Django 3.0.8 on 2020-09-01 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0011_auto_20200830_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='payment',
            field=models.CharField(choices=[('yearly', 'Yearly'), ('monthly', 'Monthly'), ('only_piqlfilm', 'Only piqlFilm'), ('only_piqlreader', 'Only piqlReader')], max_length=40, verbose_name='Payment'),
        ),
    ]
