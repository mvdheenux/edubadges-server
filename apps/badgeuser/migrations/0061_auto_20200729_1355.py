# Generated by Django 2.2.13 on 2020-07-29 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('badgeuser', '0060_auto_20200729_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='termsagreement',
            name='terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='badgeuser.Terms'),
        ),
    ]