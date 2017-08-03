from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Snippet, Admin
from .serializers import SnippetSerializer, AdminSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


@csrf_exempt
def admin_create(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=401) # 401 just for test
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def admin_set_profile(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            snippet = Admin.objects.get(email = data['email'])
            serializer1 = AdminSerializer(snippet, data = data)
            if serializer1.is_valid():
                serializer1.save()
                return JsonResponse(serializer1.data, status = 401) # 401 just for test
            return JsonResponse(serializer1.errors, status = 400)
        except Admin.DoesNotExist:
            return HttpResponse(status=404)


@csrf_exempt
def admin_login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        # TODO add SHA512 fuction

        try:
            snippet = Admin.objects.get(email = data['email'], password = data['password'])
            return HttpResponse("Valid", status = 401)  # 401 just for test
        except Admin.DoesNotExist:
            return HttpResponse("Invalid", status = 400)


@csrf_exempt
def admin_reset_password(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AdminSerializer(data=data)

        # TODO add SHA512 fuction

        try:
            snippet = Admin.objects.get(email = data['email'], password = data['password'])
            data['password'] = data['newpassword']
            serializer = AdminSerializer(snippet, data = data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status = 401) # 401 just for test
            return HttpResponse("Completed", status = 400)
        except Admin.DoesNotExist:
            return HttpResponse("Wrong Password or Email", status = 400)