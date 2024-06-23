from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response

from hiringProject.models import IhaFeatures, User
from hiringProject.serializers import IhaFeaturesSerializer
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]
        print(request)
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, 'Geçersiz kullanıcı adı veya parola.')
    return render(request, 'login.html')

def logout(request):
    logout(request)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'register.html', {'message': 'Username kullanılıyor'})
            elif User.objects.filter(email=email).exists():
                return render(request, 'register.html', {'message': 'Email kullanılıyor'})
            else:
                user = User(username=username, email=email, firstName=first_name, lastName=last_name)
                user.password = make_password(password)  # Şifreyi hashle ve sakla
                user.save()
                login(request, user)  # Kayıt olduktan sonra otomatik giriş yap
                return redirect('home')  # Ana sayfaya yönlendir
        else:
            return render(request, 'register.html', {'message': 'Hatali parola'})
    else:
        return render(request, 'register.html')
    

def ihaFeatures(request):
    queryset = IhaFeatures.objects.all()
    serializer_class = IhaFeaturesSerializer
    return render(request,'iha_features.html')

@api_view(['GET', 'POST'])
def getAndSaveIhaFeatures(request):
     if request.method == 'GET':
        ihas= IhaFeatures.objects.all()
        serializer = IhaFeaturesSerializer(ihas, many=True)
        return Response(serializer.data)
     
     elif request.method == 'POST':
        serializer = IhaFeaturesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
     
def ihafeatures_view(request):
    return render(request, 'iha_features.html')
