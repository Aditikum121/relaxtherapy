# Generated by Django 5.0.2 on 2024-05-18 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Service_icon', models.CharField(max_length=50)),
                ('Service_tittle', models.CharField(max_length=50)),
                ('Service_des', models.TextField()),
            ],
        ),
    ]
