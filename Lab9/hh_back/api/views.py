from django.http import JsonResponse
from .models import Company, Vacancy

def api_home(request):
    message = {
        'message': 'Welcome to the HeadHunter API!',
        'endpoints': {
            'Companies': {
                'List all Companies': '/api/companies/',
                'Get one Company': '/api/companies/<int:id>/',
                'List Vacancies by Company': '/api/companies/<int:id>/vacancies/',
            },
            'Vacancies': {
                'List all Vacancies': '/api/vacancies/',
                'Get one Vacancy': '/api/vacancies/<int:id>/',
                'List Top 10 Vacancies': '/api/vacancies/top_ten/',
            }
        }
    }
    return JsonResponse(message)

def company_list(request):
    companies = Company.objects.all()
    data = {'companies': list(companies.values())}
    return JsonResponse(data)

def company_detail(request, id):
    try:
        company = Company.objects.get(id=id)
        data = {'company': {
            'name': company.name,
            'description': company.description,
            'city': company.city,
            'address': company.address
        }}
        return JsonResponse(data)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company does not exist'}, status=404)

def company_vacancies(request, id):
    try:
        company = Company.objects.get(id=id)
        vacancies = company.vacancies.all()
        data = {'vacancies': list(vacancies.values())}
        return JsonResponse(data)
    except Company.DoesNotExist:
        return JsonResponse({'error': 'Company does not exist'}, status=404)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    data = {'vacancies': list(vacancies.values())}
    return JsonResponse(data)

def vacancy_detail(request, id):
    try:
        vacancy = Vacancy.objects.get(id=id)
        data = {'vacancy': {
            'name': vacancy.name,
            'description': vacancy.description,
            'salary': vacancy.salary,
            'company': vacancy.company.name
        }}
        return JsonResponse(data)
    except Vacancy.DoesNotExist:
        return JsonResponse({'error': 'Vacancy does not exist'}, status=404)

def top_ten_vacancies(request):
    top_vacancies = Vacancy.objects.order_by('-salary')[:10]
    data = {'vacancies': list(top_vacancies.values())}
    return JsonResponse(data)
