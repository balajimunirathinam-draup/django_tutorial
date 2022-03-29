# Generated by Django 4.0.3 on 2022-03-01 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Population',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('human_count', models.PositiveBigIntegerField()),
            ],
        ),
    ]
