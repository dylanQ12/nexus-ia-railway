# Generated by Django 4.2 on 2024-05-05 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_servicio_link_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicio',
            name='link_pdf',
        ),
    ]
