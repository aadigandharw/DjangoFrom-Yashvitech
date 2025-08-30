from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

# Create your views here.
# def Home(request):
#     return HttpResponse("Hello World")

# def register(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         user_class = request.POST.get('user_class')
#         address = request.POST.get('address')

#         # Create new user
#         Registration.objects.create(name=name, email=email, user_class= user_class, address = address)
#         return render(request, 'index.html', {'success': 'Registration successful!'})

#     return render(request, 'index.html')



# class RegisterApiView(APIView):
#     def get(self ,request,id=None):

#         if id:
#             data = get_object_or_404(Registration,pk=id)
#             serialized_data = RegisterSerializers(data)
#             return Response(serialized_data.data)
#         else:
#             data = Registration.objects.all()
#             serialized_data = RegisterSerializers(data,many=True)
#             return Response(serialized_data.data)
    
#     def post(self,request):
#         serialized_data = RegisterSerializers(data =request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response("Success")
#         else:
#             return Response("Invalid Data")
        

#     def put(self,request,id=None):
#         old_data = get_object_or_404(Registration,pk=id)

#         serialized_data = RegisterSerializers(old_data,data=request.data)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response("Saved Successfully")
#         else:
#             return Response("Not Saved Successfully")
        


#     def patch(self,request,id=None):
#         old_data = get_object_or_404(Registration,pk=id)

#         serialized_data = RegisterSerializers(old_data,data=request.data,partial=True)
#         if serialized_data.is_valid():
#             serialized_data.save()
#             return Response("Saved Successfully")
#         else:
#             return Response("Not Saved Successfully")
        

#     def delete(self,request,id=None):
#         if id:
#             old_data = get_object_or_404(Registration,pk=id)
#             old_data.delete()
#             return Response("Successfully Deleted")
#         else:
#             return Response("Not Deleted")
            

# class StudentApiView(APIView):
#     def get(self ,request):

#         data = StudentLogin.objects.all()
#         serialized_data = StudentSerializers(data,many=True)
#         return Response(serialized_data.data)


class MyUserApiView(APIView):
    def get(self,request,id=None):
        if id:
            data = get_object_or_404(MyUser,pk=id)
            serializer = MyUserSerializers(data)
            return Response(serializer.data)        
        else:
            data = MyUser.objects.all()
            serializer = MyUserSerializers(data,many=True)
            return Response(serializer.data)
        

    def post(self,request):
        serializer = MyUserSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Has Been Saved")
        else:
            return Response("Not Saved!!!")
        
    
    def put(self,request,id=None):
        currentData = get_object_or_404(MyUser,pk=id)
        serializer = MyUserSerializers(currentData,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Has Been Updated")
        else:
            return Response("Not Updated")
        

    def patch(self,request,id=None):
        currentData = get_object_or_404(MyUser,pk=id)
        serializer = MyUserSerializers(currentData,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response("Data Has Been Updated")
        else:
            return Response("Not Updated")
        

    def delete(self,reuqest,id=None):
        currentData = get_object_or_404(MyUser,pk=id)
        currentData.delete()
        return Response("Data Has been deleted")



