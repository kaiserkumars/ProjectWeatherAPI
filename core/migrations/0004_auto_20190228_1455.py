# Generated by Django 2.0.3 on 2019-02-28 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190228_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='month',
            field=models.IntegerField(max_length=2),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='year',
            field=models.IntegerField(max_length=4),
        ),
    ]
