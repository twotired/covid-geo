# Generated by Django 3.2.5 on 2021-09-04 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uscensus', '0002_alter_population_popestimate2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='population',
            name='census2010pop',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='population',
            name='popestimate2010',
            field=models.IntegerField(),
        ),
    ]