# Generated by Django 5.0.6 on 2024-06-12 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='unias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=20)),
                ('largo', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=20)),
            ],
        ),
    ]
