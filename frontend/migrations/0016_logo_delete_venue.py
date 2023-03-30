# Generated by Django 4.1.7 on 2023-03-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0015_venue'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo_image', models.ImageField(blank=True, null=True, upload_to='Static/IMG/')),
            ],
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
