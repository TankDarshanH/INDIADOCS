# Generated by Django 5.0.2 on 2024-04-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_alter_package_file_size_alter_package_max_uploads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='file_size',
            field=models.BigIntegerField(blank=True, default='unlimited', null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='max_uploads',
            field=models.IntegerField(blank=True, default='unlimited', null=True),
        ),
    ]
