# Generated by Django 5.0.3 on 2024-03-22 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Jaihanuman_Purifiers', '0002_feedback_alter_serivce_address_alter_serivce_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='Name',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
