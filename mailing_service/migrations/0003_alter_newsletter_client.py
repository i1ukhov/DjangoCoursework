# Generated by Django 5.0.6 on 2024-05-25 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing_service', '0002_alter_newsletter_client_alter_newsletter_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='client',
            field=models.ManyToManyField(blank=True, to='mailing_service.client', verbose_name='клиент'),
        ),
    ]
