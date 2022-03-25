# Generated by Django 3.2.4 on 2021-06-21 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ai', '0002_alter_members_flat_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='email_id',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='members',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AddField(
            model_name='vehicles',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]