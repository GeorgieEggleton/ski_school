# Generated by Django 3.2.23 on 2023-12-19 11:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lessons', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('country', django_countries.fields.CountryField(max_length=2)),
                ('postcode', models.CharField(blank=True, max_length=20, null=True)),
                ('dateTimeCreated', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('stripe_pid', models.CharField(default='', max_length=254)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderLineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lineitem_total', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('lesson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lessons.lesson')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineitems', to='payment.order')),
                ('students', models.ManyToManyField(blank=True, to='lessons.Student')),
            ],
        ),
    ]
