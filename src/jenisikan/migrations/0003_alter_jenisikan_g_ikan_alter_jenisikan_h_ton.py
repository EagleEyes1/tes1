# Generated by Django 4.0.3 on 2022-06-23 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jenisikan', '0002_alter_jenisikan_h_ton'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jenisikan',
            name='g_ikan',
            field=models.CharField(max_length=999999999),
        ),
        migrations.AlterField(
            model_name='jenisikan',
            name='h_ton',
            field=models.IntegerField(),
        ),
    ]
