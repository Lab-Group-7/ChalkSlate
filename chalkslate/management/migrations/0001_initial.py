# Generated by Django 3.0.1 on 2020-02-11 21:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChalkSlateUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=60, unique=True)),
                ('date_joined', models.DateField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=60, verbose_name='first name')),
                ('last_name', models.CharField(max_length=60, verbose_name='last name')),
                ('user_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Authority (superuser or admin)'), (2, 'ChalkSlateAdmin'), (3, 'Student'), (4, 'Tutor')], null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ChalkSlateAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=100, unique=True, verbose_name='institute name')),
                ('institute_details', models.CharField(max_length=100, verbose_name='institute details')),
                ('chalkslate_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tutor_details', models.CharField(max_length=100, verbose_name='tutor details')),
                ('picture', models.ImageField(upload_to='tutor_pictures', verbose_name='picture')),
                ('chalkslate_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_details', models.CharField(max_length=100, verbose_name='student details')),
                ('picture', models.ImageField(upload_to='student_pictures', verbose_name='picture')),
                ('chalkslate_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='InsTutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.ChalkSlateAdmin')),
                ('tutor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.Tutor')),
            ],
        ),
        migrations.CreateModel(
            name='InsStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.IntegerField()),
                ('class_year', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.ChalkSlateAdmin')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='management.Student')),
            ],
            options={
                'unique_together': {('roll', 'class_year', 'section')},
            },
        ),
    ]
