# Generated by Django 5.1.5 on 2025-01-18 12:34

from django.db import migrations

from django.contrib.auth.models import User

def create_default_admin(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.create_superuser(
        username='admin',
        email='admin@example.com',
        password='adminpassword'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('draws', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_admin),
    ]
