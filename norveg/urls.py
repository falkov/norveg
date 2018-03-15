"""norveg URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

import app_main.views
import app_quiz.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('learning/<int:section_number>/<int:question_num_in_section>/', app_quiz.views.learning, name='learning'),
    path('testing/<str:new_test>/<int:question_number>/', app_quiz.views.testing, name='testing'),
    path('testing/<str:new_test>/<int:question_number>/<slug:user_answer>/', app_quiz.views.testing, name='testing'),
    path('endtest/<slug:user_answer>/', app_quiz.views.end_test, name='end-test'),
    # path('endtest/<slug:user_answer>/<str:show_question>/', app_quiz.views.end_test, name='end-test'),
    path('home/', app_main.views.home, name='home'),
]

