# Generated by Django 4.1.7 on 2023-03-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0014_rename_field100_active_selecting_fields_field1_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_image', models.ImageField(blank=True, null=True, upload_to='IMG/')),
            ],
        ),
    ]
