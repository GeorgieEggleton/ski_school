# Generated by Django 3.2.23 on 2023-12-11 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0015_auto_20231211_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.DateField(),
        ),
    ]