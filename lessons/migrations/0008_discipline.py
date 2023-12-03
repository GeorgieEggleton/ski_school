# Generated by Django 3.2.23 on 2023-12-03 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0007_lessontype_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Ski', max_length=128)),
                ('equipment_type', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
    ]
