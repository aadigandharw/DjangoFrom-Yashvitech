from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def Home(request):
    return HttpResponse("Hello World")

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        user_class = request.POST.get('user_class')
        address = request.POST.get('address')

        # Create new user
        Registration.objects.create(name=name, email=email, user_class= user_class, address = address)
    

        return render(request, 'index.html', {'success': 'Registration successful!'})

    return render(request, 'index.html')



class RegisterApiView(APIView):
    def get(self , request):

        data = Registration.objects.all()
        serialized_data = RegisterSerializers(data,many=True)
        return Response(serialized_data.data)
    
class StudentApiView(APIView):
    def get(self , request):

        data = StudentLogin.objects.all()
        serialized_data = StudentSerializers(data,many=True)
        return Response(serialized_data.data)