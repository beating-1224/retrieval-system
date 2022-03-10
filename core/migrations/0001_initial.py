# Generated by Django 3.1.1 on 2022-03-08 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasetName', models.CharField(max_length=100, verbose_name='dataset name')),
            ],
            options={
                'verbose_name': 'Dataset Information',
                'verbose_name_plural': 'Dataset Information',
            },
        ),
    ]