# Generated by Django 3.0.8 on 2020-10-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0015_input_production'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='production',
            field=models.CharField(choices=[('Norway', 'Piql Norway'), ('Slovakia', 'Piql Slovakia'), ('Mexico', 'Piql Mexico')], default='Norway', max_length=40, verbose_name='Production partner:'),
        ),
    ]
