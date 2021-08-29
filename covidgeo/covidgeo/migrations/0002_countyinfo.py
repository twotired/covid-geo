# Generated by Django 3.2.5 on 2021-08-23 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('covidgeo', '0001_custom_migration'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geoid', models.IntegerField()),
                ('state', models.CharField(max_length=128)),
                ('county', models.CharField(max_length=256)),
                ('statefp', models.IntegerField()),
                ('countyfp', models.IntegerField()),
                ('census2010pop', models.IntegerField()),
                ('popestimate2019', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'CountiesInfo',
                'managed': False,
            },
        ),
    ]