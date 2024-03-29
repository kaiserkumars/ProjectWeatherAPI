# Generated by Django 2.0.3 on 2019-03-03 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('metric', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('value', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='weatherdata',
            unique_together={('location', 'metric', 'date')},
        ),
    ]
