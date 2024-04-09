from django.http import JsonResponse
from .models import Category, Product

def product_list(request):
    products = Product.objects.all()
    data = [{'id': product.id, 'name': product.name} for product in products]
    return JsonResponse(data, safe=False)

def product_detail(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = {'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description, 'count': product.count, 'is_active': product.is_active}
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

def category_list(request):
    categories = Category.objects.all()
    data = [{'id': category.id, 'name': category.name} for category in categories]
    return JsonResponse(data, safe=False)

def category_detail(request, id):
    try:
        category = Category.objects.get(pk=id)
        data = {'id': category.id, 'name': category.name}
        return JsonResponse(data)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

def category_products(request, id):
    try:
        category = Category.objects.get(pk=id)
        products = category.products.all()
        data = [{'id': product.id, 'name': product.name} for product in products]
        return JsonResponse(data, safe=False)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)
