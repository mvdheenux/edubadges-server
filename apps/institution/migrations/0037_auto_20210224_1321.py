# Generated by Django 2.2.14 on 2021-02-24 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0036_auto_20210224_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='name_english',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
