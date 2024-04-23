# Generated by Django 5.0.4 on 2024-04-23 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gyms', '0014_trainer_map_alter_service_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='map',
        ),
        migrations.AddField(
            model_name='gym',
            name='map',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='gym',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images/'),
        ),
    ]