# Generated by Django 5.0.4 on 2024-04-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_permission_subscription_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='permission',
            name='start_date',
            field=models.DateField(),
        ),
    ]