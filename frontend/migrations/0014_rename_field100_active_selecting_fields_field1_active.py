# Generated by Django 4.1.7 on 2023-03-29 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0013_rename_field1_active_selecting_fields_field100_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='selecting_fields',
            old_name='field100_active',
            new_name='field1_active',
        ),
    ]
