"""ref_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from .views import main_view,signup_view
from profiles.views import *
from core.views import checkout, success
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view, name='main-view'),
    path('signup/', signup_view, name='signup-view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login-view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout-view'),
    path('profiles/', my_recommendations_view, name='my-recs-view'),
    path('task-list/', task_list, name='task_list'),  # Define the task list URL above the main view URL
    path('payment/', checkout, name="checkout"),
    path('success', success, name="success"),
    path('<str:ref_code>/', main_view, name='main-view'),
    path('tasks/create/', create_task, name='create_task'),
]
