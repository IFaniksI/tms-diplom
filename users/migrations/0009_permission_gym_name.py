# Generated by Django 5.0.4 on 2024-04-22 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_permission_subscription_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='gym_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]