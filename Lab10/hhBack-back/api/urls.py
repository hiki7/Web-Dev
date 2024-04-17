from django.urls import path, re_path
from api import views,fbv,cbv
# from cbv import VacancyListAPIView
urlpatterns = [
    path('companies/', fbv.companies_list),
    path('companies/<int:id>/vacancies/',views.company_vacancy),
    path('companies/<int:id>/', fbv.company_by_id),
    path('vacancies/', cbv.VacancyListAPIView.as_view()),
    path('vacancies/<int:id>/',cbv.VacancyByIdAPIView.as_view()),
    path('vacancies/top_ten/', views.top_ten)
]