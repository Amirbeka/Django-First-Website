# Generated by Django 4.0.3 on 2022-03-24 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ism',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=40)),
                ('familiya', models.CharField(max_length=40)),
                ('ty', models.IntegerField()),
            ],
        ),
    ]
