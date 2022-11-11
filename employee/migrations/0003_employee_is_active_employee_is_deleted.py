# Generated by Django 4.1.3 on 2022-11-11 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_alter_employee_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]