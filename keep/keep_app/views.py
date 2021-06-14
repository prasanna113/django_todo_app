from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from keep_app.models import KeepApp
from keep_app.serializers import KeepSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def todo_list(request):

    if request.method == 'GET':
        todo = KeepApp.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            todo = todo.filter(title__icontains=title)

        todo_serializer = KeepSerializer(todo, many=True)
        return JsonResponse(todo_serializer.data, safe=False)

    elif request.method == 'POST':
        todo_data = JSONParser().parse(request)
        todo_serializer = KeepSerializer(data=todo_data)

        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = KeepApp.objects.all().delete()
        return JsonResponse({'message': '{} ToDos were deleted successfully'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_list_details(request, pk):
    try:
        todo = KeepApp.objects.get(pk=pk)
    except KeepApp.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        todo_serializer = KeepSerializer(todo)
        return JsonResponse(todo_serializer.data)

    elif request.method == 'PUT':
        todo_data = JSONParser().parse(request)
        todo_serializer = KeepSerializer(todo, data=todo_data)

        if todo_serializer.is_valid():
            todo_serializer.save()
            return JsonResponse(todo_serializer.data)
        return JsonResponse(todo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        todo.delete()
        return JsonResponse({'message': 'ToDo was deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def todo_completed(request):
    todo = KeepApp.objects.filter(status=True)

    if request.method == 'GET':
        todo_serializer = KeepSerializer(todo, many=True)
        return JsonResponse(todo_serializer.data, safe=False)
