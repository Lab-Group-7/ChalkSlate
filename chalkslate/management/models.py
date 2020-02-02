from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class ChalkSlateUser(AbstractUser):

    INSTITUTE = 1
    STUDENT = 2
    TUTOR = 3

    USER_TYPE_CHOICES = (

        (INSTITUTE, 'Admin'),
        (STUDENT, 'Student'),
        (TUTOR, 'Tutor'),

    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    # is_admin = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=False)
    # is_tutor = models.BooleanField(default=False)

class Admin(models.Model):
    chalkslate_user = models.OneToOneField(ChalkSlateUser, on_delete=models.CASCADE)
    username_institute = models.CharField(max_length=100, unique=True)
    institute_name = models.CharField(max_length=100, unique=True)
    institute_details = models.CharField(max_length=100)

    def __str__(self):
        return self.institute_name

class Student(models.Model):
    chalkslate_user = models.OneToOneField(ChalkSlateUser, on_delete=models.CASCADE)
    username_student = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    student_details = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='student_pictures')

    def __str__(self):
        return self.name

class Tutor(models.Model):
    chalkslate_user = models.OneToOneField(ChalkSlateUser, on_delete=models.CASCADE)
    username_tutor = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    tutor_details = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='tutor_pictures')

    def __str__(self):
        return self.name

# make the ins_tutor and ins_student models

class InsStudent(models.Model):
    institute = models.ForeignKey(Admin, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    roll = models.IntegerField()
    class_year = models.CharField(max_length=50)
    section = models.CharField(max_length=50)

    class Meta:
        unique_together = ('roll', 'class_year', 'section',)

class InsTutor(models.Model):
    institute = models.ForeignKey(Admin, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)