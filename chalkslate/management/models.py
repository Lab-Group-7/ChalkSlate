from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class MyAccountManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("Users must have an email address.")
        if not username:
            raise ValueError("Users must have a username.")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )

        user.user_type = 1

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)





class ChalkSlateUser(AbstractBaseUser):

    # required to include
    email = models.EmailField(verbose_name='email', unique=True, max_length=60)
    username = models.CharField(max_length=60, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    # new
    first_name = models.CharField(max_length=60, verbose_name='first name')
    last_name = models.CharField(max_length=60, verbose_name='last name')
    has_institute = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    AUTHORITY = 1
    INSTITUTE = 2
    STUDENT = 3
    TUTOR = 4

    USER_TYPE_CHOICES = (

        (AUTHORITY, 'Authority (superuser or admin)'),
        (INSTITUTE, 'ChalkSlateAdmin'),
        (STUDENT, 'Student'),
        (TUTOR, 'Tutor'),

    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True)
    # user_type = models.PositiveSmallIntegerField(null=True, blank=True)

    # is_admin = models.BooleanField(default=False)
    # is_student = models.BooleanField(default=False)
    # is_tutor = models.BooleanField(default=False)

class ChalkSlateAdmin(models.Model):
    chalkslate_user = models.OneToOneField(ChalkSlateUser, on_delete=models.CASCADE, null=True)
    # username_institute = models.CharField(max_length=100, unique=True)
    institute_name = models.CharField(verbose_name='institute name', max_length=100, unique=True)
    institute_details = models.CharField(verbose_name='institute details', max_length=100)

    def __str__(self):
        return self.chalkslate_user.email

class Student(models.Model):
    chalkslate_user = models.OneToOneField(ChalkSlateUser, on_delete=models.CASCADE)
    # username_student = models.CharField(max_length=100, unique=True)
    # name = models.CharField(max_length=100)
    student_details = models.CharField(verbose_name='student details', max_length=100)
    picture = models.ImageField(verbose_name='picture', upload_to='student_pictures')

    def __str__(self):
        return self.chalkslate_user.email

class Tutor(models.Model):
    chalkslate_user = models.OneToOneField(ChalkSlateUser, on_delete=models.CASCADE)
    # username_tutor = models.CharField(max_length=100, unique=True)
    # name = models.CharField(max_length=100)
    tutor_details = models.CharField(verbose_name='tutor details', max_length=100)
    picture = models.ImageField(verbose_name='picture', upload_to='tutor_pictures')
    institute = models.ForeignKey(ChalkSlateAdmin, on_delete=models.SET_NULL, null=True, default=None)

    def __str__(self):
        return self.chalkslate_user.email

# make the ins_tutor and ins_student models

class InsStudent(models.Model):
    institute = models.ForeignKey(ChalkSlateAdmin, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    roll = models.IntegerField()
    class_year = models.CharField(max_length=50)
    section = models.CharField(max_length=50)

    class Meta:
        unique_together = ('roll', 'class_year', 'section',)

class InsTutor(models.Model):
    institute = models.ForeignKey(ChalkSlateAdmin, on_delete=models.CASCADE)
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)

class notice(models.Model):
    name=models.CharField(max_length=50,null=False)
    mail=models.CharField(max_length=50,null=False)
    date=models.DateTimeField(null=False)
    content=models.CharField(max_length=200,null=False)
    per=models.CharField(max_length=50,default='no')
    def __str__(self):
        return self.name


class TutorApplication(models.Model):
    institute = models.ForeignKey(ChalkSlateAdmin, on_delete=models.CASCADE)
    tutor = models.OneToOneField(Tutor, on_delete=models.CASCADE)
    note = models.TextField(max_length=100)
    posted = models.DateTimeField(auto_now_add=True)

class StudentApplication(models.Model):
    institute = models.ForeignKey(ChalkSlateAdmin, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    note = models.CharField(max_length=100)
    posted = models.DateTimeField(auto_now_add=True)