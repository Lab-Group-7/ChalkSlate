from django.contrib import admin
from .models import ChalkSlateUser, ChalkSlateAdmin, Student, Tutor, InsStudent, InsTutor, notice, TutorApplication, StudentApplication

# Register your models here.

admin.site.register(ChalkSlateUser)
admin.site.register(ChalkSlateAdmin)
admin.site.register(Student)
admin.site.register(Tutor)
admin.site.register(InsStudent)
admin.site.register(InsTutor)
admin.site.register(notice)
admin.site.register(TutorApplication)
admin.site.register(StudentApplication)