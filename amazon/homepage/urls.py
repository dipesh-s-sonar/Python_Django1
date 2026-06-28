"""
URL configuration for amazon project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='Home page'),
    path('about/',views.about,name='About Us page'),
    path('contact/',views.contact,name='Contact page'),
    path('services/',views.services,name='Services page'),
    path('registration/',views.registration,name='Registration Page'),
    path('square/',views.square,name='Square Page'),
    path('output/', views.output, name='Output Page'),
    path('addition/', views.addition, name='addition Page'),
    path('add_op/', views.add_op, name='add_op Page'),
    path('login/', views.login, name='Login Page'),
    path('admindashboard/', views.admindashboard, name='Admin Dashboard Page'),
    path('addemp/', views.addemp, name='Add Employee Page'),
    path('saveemp/', views.saveemp, name='saveemp'),
    path('empshow/',views.admin_show_emp,name='Show Single Employee Page'),
    path('adminsingle/<int:id>',views.admin_single_emp, name='Single Employee Page'),
    path('empdelete/<int:id>',views.admin_delete_emp,name='Delete Single Employee Page'),
    path('admin_update_emp/',views.admin_update_emp,name='Update Single Employee Page'),
]
