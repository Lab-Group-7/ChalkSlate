from django.contrib import admin
from .models import ChalkSlateUser, Admin, Student, Tutor, InsStudent, InsTutor

# Register your models here.

admin.site.register(ChalkSlateUser)
admin.site.register(Admin)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(InsStudent)
admin.site.register(InsTutor)