# Generated by Django 3.2.23 on 2023-12-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0011_alter_lessontype_age_range'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='places_taken',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
