from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import User  # Make sure your User model is imported
from .serializers import UserSerializer  # Ensure this is the correct import


# Create your views here.
def home(request):
    return render(request, "api/home.html")


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def user_api(request):
    users = User.objects.all()

    if request.method == 'GET':
        serializer = UserSerializer(users, many=True)  # Corrected the typo here
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)  # Corrected the typo here
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        users.delete()
        return Response(status=204)

    elif request.method == 'PUT':
        serializer = UserSerializer(data=request.data)  # Corrected the typo here
        if serializer.is_valid():
            serializer.save()  # update
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
