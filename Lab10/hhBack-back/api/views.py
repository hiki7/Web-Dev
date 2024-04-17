from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse 
from api.models import Company, Vacancy
from api.serializers import CompanySerializer1,CompanySerializer2
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

# @csrf_exempt
# def companies_list(request):
#     if request.method == 'GET':
#         companies = Company.objects.all()
#         serializer = CompanySerializer1(companies,many=True)
#         return JsonResponse(
#             serializer.data, safe=False,json_dumps_params={'indent' : 2}
#         )
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         serializer = CompanySerializer1(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#         # company_name = data.get('name','')
#         # company = Company.objects.create(name=company_name)
#         # return JsonResponse(company.to_json(), safe=False,json_dumps_params={'indent' : 2})
# @csrf_exempt
# def company_by_id(request,id):
#     try:
#         company = Company.objects.get(id=id)
#     except:
#         return HttpResponse('do not have such id')
#     if request.method == 'GET':
#         serializer = CompanySerializer2(company,many=False)
#         return JsonResponse(serializer.data, safe=False,json_dumps_params={'indent' : 2})
#     if request.method == 'DELETE':
#         company.delete()
#         return JsonResponse({'deleted': True})
#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         serializer = CompanySerializer2(instance=company,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
        # new_company_name = data.get('name', company.name)
        # company.name = new_company_name
        # company.save()
        # return JsonResponse(company.to_json())
    # for i in list(Company.objects.values()):
    #     if str(i['id']) == str(id):
    #         return JsonResponse(i,safe=False,json_dumps_params={'indent' : 2})
    # return HttpResponse('do not have such id')
@csrf_exempt
def company_vacancy(request,id):
    if request.method == 'GET':
        temp = []
        for i in list(Vacancy.objects.values()):
            if str(i['company_id']) == str(id):
                temp.append(i)
        # if len(temp) != 0:
        return JsonResponse(temp, safe=False, json_dumps_params={'indent' : 2})
        # else:
        #     return HttpResponse('No vacancies')
# @csrf_exempt
# def vacancies_list(request):
#     if request.method == 'GET':
#         return JsonResponse(
#             Vacancy.objects.values(), safe=False,json_dumps_params={'indent' : 2}
#         )
    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     vacancy_name = data.get('name', '')
    #     vacancy_company = Company.objects.get(id=data.get('company',''))
    #     vacancy = Vacancy.objects.create(name=vacancy_name,company=vacancy_company)
    #     return JsonResponse(vacancy.to_json(), safe=False,json_dumps_params={'indent' : 2})
# @csrf_exempt
# def vacancy_by_id(request,id):
#     try:
#         vacancy = Vacancy.objects.get(id=id)
#     except:
#         return HttpResponse('do not have such id')
#     if request.method == 'GET':
#         return JsonResponse(vacancy.to_json(), safe=False)
#     if request.method == 'DELETE':
#         vacancy.delete()
#         return JsonResponse({'deleted': True})
#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         new_vacancy_name = data.get('name', vacancy.name)
#         # desc = data.get('desc', category.desc)
#         vacancy.name = new_vacancy_name
#         vacancy.save()
#         return JsonResponse(vacancy.to_json())
@csrf_exempt
def top_ten(request):
    return JsonResponse(
        list(Vacancy.objects.order_by('-salary')[:10].values()), safe=False, json_dumps_params={'indent' : 2}
    )