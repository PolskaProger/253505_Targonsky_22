# Generated by Django 4.2.5 on 2023-09-25 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_job_promotional_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='is_actual',
            field=models.BooleanField(default=True, help_text='Is actual?'),
        ),
    ]
