# Generated by Django 2.0.6 on 2018-06-09 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CallApi', '0003_auto_20180609_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('number_of_employees', models.IntegerField()),
                ('employees_avarage_salary', models.IntegerField()),
            ],
        ),
    ]