# Generated by Django 5.0.4 on 2024-04-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0005_remove_service_gym_gym_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gym',
            name='service',
        ),
        migrations.AddField(
            model_name='gym',
            name='service',
            field=models.ManyToManyField(related_name='gym', to='gyms.service'),
        ),
    ]
