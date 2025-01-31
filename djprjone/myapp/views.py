from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def home_func(request):
    if request.method == 'GET':
        return JsonResponse({"msg": "Hello from Home"}, status=200)
    else:
        return JsonResponse({"msg": "Invalid Request Method"}, status=405)


@csrf_exempt
def http_func(request):
    if request.method == 'GET':
        return JsonResponse({"msg": "accessing through GET HTTP method"}, status=200)
    if request.method == 'POST':
        return JsonResponse({"msg": "accessing through POST HTTP method"}, status=201)
    if request.method == 'PUT':
        return JsonResponse({"msg": "accessing through PUT HTTP method"}, status=201)
    if request.method == 'PATCH':
        return JsonResponse({"msg": "accessing through PATCH HTTP method"}, status=201)
    if request.method == 'DELETE':
        return JsonResponse({"msg": "accessing through DELETE HTTP method"}, status=200)

