# Generated by Django 4.2.7 on 2024-01-11 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='patient/images'),
        ),
    ]
