# Generated by Django 5.0.2 on 2024-02-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0006_alter_cropschedule_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cropschedule',
            name='description',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
