"""chalkslate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.start),


    path('chalkslate/', include('management.urls')),

    #firstPage

    #menu
    # path('home/', views.home),
    # path('notice-board/', views.notice_board),
    # path('guide/', views.guide),
    # path('about-us/', views.about_us),
    # path('contact-us/', views.contact_us),
    # path('signin/', views.signin),
    # path('register/', views.register),
    #
    # path('reg-admin/', views.reg_admin),
    # path('reg-tutor/', views.reg_tutor),
    # path('reg-student/', views.reg_student),
    #
    # path('home-admin/', views.home_admin),
    # path('home-tutor/', views.home_tutor),
    # path('home-student/', views.home_student),
    #
    # path('home-admin-notice/', views.home_admin_notice),
    # path('home-admin-class/', views.home_admin_class),
    # path('home-admin-tutor/', views.home_admin_tutor),
    # path('home-admin-result/', views.home_admin_result),
    # path('home-admin-other/', views.home_admin_other),
    #
    # path('home-tutor-notice/', views.home_tutor_notice),
    # path('home-tutor-class/', views.home_tutor_class),
    # path('home-tutor-attendance/', views.home_tutor_attendance),
    # path('home-tutor-result/', views.home_tutor_result),
    # path('home-tutor-other/', views.home_tutor_other),
    #
    # path('home-student-notice/', views.home_student_notice),
    # path('home-student-feedback/', views.home_student_feedback),
    # path('home-student-result/', views.home_student_result),
    # path('home-student-other/', views.home_student_other),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
