# Generated by Django 3.2.5 on 2021-08-09 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PresidentCounty2020',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=32)),
                ('county', models.CharField(max_length=128)),
                ('candidate', models.CharField(max_length=128)),
                ('total_votes', models.IntegerField()),
                ('won', models.BooleanField()),
            ],
            options={
                'unique_together': {('state', 'county', 'candidate')},
            },
        ),
    ]
