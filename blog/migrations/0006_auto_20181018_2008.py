# Generated by Django 2.1.1 on 2018-10-18 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181018_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bomsheet',
            name='father',
        ),
        migrations.RemoveField(
            model_name='bomsheet',
            name='son',
        ),
        migrations.DeleteModel(
            name='BOMSheet',
        ),
        migrations.DeleteModel(
            name='ItemSheet',
        ),
    ]
