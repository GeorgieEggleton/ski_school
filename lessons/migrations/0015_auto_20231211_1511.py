# Generated by Django 3.2.23 on 2023-12-11 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lessons', '0014_student_useraccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='remaining_capacity',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='userAccount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
