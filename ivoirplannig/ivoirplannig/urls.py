"""
URL configuration for ivoirplannig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from delta.views import index, login,admin_role,admin_secure,admin_user,para_prof,para_cours,para_groupes,para_mat, rlt_groupes ,rlt_prof,register

urlpatterns = [
    path('delta-admin/', admin.site.urls),
    path('account/login',login,name="login"),
    path('register',login,name="login"),
    
    path('admin_role',admin_role,name="role"),
    path('admin_secure',admin_secure,name="secure"),
    path('admin_user',admin_user,name="user"),
    
      path('param/professeur',para_prof,name="prof"),
      path('param/cours',para_cours,name="cours"),
      path('param/groupes',para_groupes,name="groupes"),
      path('param/matiere',para_mat,name="mat"),
    
    
      path('resltat/groupes',rlt_groupes,name="rltgroupes"),
      path('resulta/traitement',rlt_prof,name="prof"),
    
    path('',login,name='home'),
    path('register',register,name='register'),
        
    path('home',index,name='tb')
]
