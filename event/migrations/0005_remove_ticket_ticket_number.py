# Generated by Django 5.0.7 on 2024-09-11 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_ticket_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_number',
        ),
    ]
