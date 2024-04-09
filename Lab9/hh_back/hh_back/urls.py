from django.urls import path
from django.contrib import admin

from api import views

urlpatterns = [
    path('', views.api_home, name='api-home'),  # Add this line for the root URL
    path('api/companies/', views.company_list, name='company-list'),
    path('api/companies/<int:id>/', views.company_detail, name='company-detail'),
    path('api/companies/<int:id>/vacancies/', views.company_vacancies, name='company-vacancies'),
    path('api/vacancies/', views.vacancy_list, name='vacancy-list'),
    path('api/vacancies/<int:id>/', views.vacancy_detail, name='vacancy-detail'),
    path('api/vacancies/top_ten/', views.top_ten_vacancies, name='top-ten-vacancies'),
    path('admin/', admin.site.urls),
]
