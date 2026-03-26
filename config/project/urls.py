"""
URL configuration for config project.

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

from src.routes.students_api import etudiants_collection, etudiants_stats, get_etudiant_by_id, search_etudiants

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/etudiants/', etudiants_collection, name='etudiants-collection'),
    path('api/etudiants/stats/', etudiants_stats, name='etudiants-stats'),
    path('api/etudiants/search/', search_etudiants, name='search-etudiants'),
    path('api/etudiants/<student_id>/', get_etudiant_by_id, name='get-etudiant-by-id'),
]
