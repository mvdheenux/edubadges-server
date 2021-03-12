# Generated by Django 2.2.14 on 2021-02-24 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('institution', '0037_auto_20210224_1321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='institution',
            old_name='image',
            new_name='image_english',
        ),
        migrations.RenameField(
            model_name='institution',
            old_name='name',
            new_name='name_english',
        ),
        migrations.AddField(
            model_name='institution',
            name='image_dutch',
            field=models.FileField(blank=True, null=True, upload_to='uploads/institution'),
        ),
        migrations.AddField(
            model_name='institution',
            name='name_dutch',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
