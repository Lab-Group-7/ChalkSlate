from django.urls import path

from . import views

urlpatterns = [
    # menu

    path('', views.first_func, name='enter_page'),
    path('home/', views.home, name='home_page'),
    path('home/notice-board/', views.notice_board),
    path('home/guide/', views.guide),
    path('home/about-us/', views.about_us),
    path('home/contact-us/', views.contact_us),
    path('home/signin/', views.signin),
    path('home/register/', views.register),

    path('reg-admin/', views.reg_admin),
    path('reg-tutor/', views.reg_tutor),
    path('reg-student/', views.reg_student),

    path('home-admin/', views.home_admin),
    path('home-tutor/', views.home_tutor),
    path('home-student/', views.home_student),

    path('home-admin-notice/', views.home_admin_notice),
    path('home-admin-class/', views.home_admin_class),
    path('home-admin-tutor/', views.home_admin_tutor),
    path('home-admin-result/', views.home_admin_result),
    path('home-admin-other/', views.home_admin_other),

    path('home-tutor-notice/', views.home_tutor_notice),
    path('home-tutor-class/', views.home_tutor_class),
    path('home-tutor-attendance/', views.home_tutor_attendance),
    path('home-tutor-result/', views.home_tutor_result),
    path('home-tutor-other/', views.home_tutor_other),

    path('home-student-notice/', views.home_student_notice),
    path('home-student-feedback/', views.home_student_feedback),
    path('home-student-result/', views.home_student_result),
    path('home-student-other/', views.home_student_other),
]