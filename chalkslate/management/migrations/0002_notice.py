# Generated by Django 2.2.7 on 2020-02-12 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('content', models.CharField(max_length=200)),
            ],
        ),
    ]
