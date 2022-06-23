# Generated by Django 4.0.3 on 2022-06-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JenisIkan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('j_ikan', models.CharField(default='', max_length=100)),
                ('g_ikan', models.BinaryField()),
                ('h_kg', models.IntegerField()),
                ('h_ton', models.IntegerField()),
            ],
        ),
    ]
