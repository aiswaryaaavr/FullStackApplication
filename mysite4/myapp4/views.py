from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import json
from .models import Register
# CSRF exempt used for testing purposes
from django.views.decorators.csrf import csrf_exempt
# http has many classes one such class is json format 
from django.http import JsonResponse
# reg user defined fn , the user should give post only as it is to register 
# data is inside request in json format , to change to python format we use json.loads() & coverts to dictionary type all data stored in data


@csrf_exempt
def reg(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        # storing each data seperately
        Fname = data.get("Fname")
        Lname = data.get("Lname")
        Phone = data.get("Phone")
        Email = data.get("Email")
        Password = data.get("Password")


# create db as register , all columns namely fname,lnmae etc should store the values passed to sep variables
        Register.objects.create(
            Fname =Fname,
            Lname =Lname,
            Phone =Phone,
            Email =Email,
            Password =Password
        )

        return JsonResponse({"message":"Registered Successfully"},status=201)
    return JsonResponse({"Error":"Post Method Only"},status=405)



@csrf_exempt

def login(request):
    if request.method == "POST":
       data = json.loads(request.body.decode("utf-8"))
       Email = data.get("Email")
       Password = data.get("Password")

       user = Register.objects.filter(Email=Email,Password=Password)
       if user:
            return JsonResponse({"message":"Login successfully"})
       else:
            return JsonResponse({"message":"Invalid Email or Password"})

    return JsonResponse({"Error":"POST method only"})



@csrf_exempt
def get_data(request):
    if request.method == "GET":
        data=Register.objects.all()
        sample = []
        for users in data:
            sample.append({
                "Firstname":users.Fname,
                "Lastname":users.Lname,
                "Phone":users.Phone,
                "Email":users.Email,
                "Password":users.Password
                })

        return JsonResponse({"Details":sample})
    return JsonResponse({"Error":"Get Method only"})    

@csrf_exempt
def delete_data(request):
    if request.method =="DELETE":
        data = json.loads(request.body.decode("utf-8"))
        Id=data.get("id")
        remove = Register.objects.filter(id=Id)
        if remove.exists():
             remove.delete()
             return JsonResponse({"message": " Deleted Successfully"})
        else :
             return JsonResponse({"message":"Deletion Unsuccessful"})
    return JsonResponse({"Error":"Delete method only"})     

@csrf_exempt
def update_data(request):
    if request.method == "PUT":
        data = json.loads(request.body.decode("utf-8"))
        Id = data.get("id")
        if not Register.objects.filter(id=Id).exists():
            return JsonResponse({"message":"User not found"})
        Register.objects.filter(id=Id).update(
            Fname = data.get("Fname"),
            Lname = data.get("Lname"),
            Phone = data.get("Phone"),
            Email = data.get("Email"),
            Password = data.get("Password")
        )
        return JsonResponse({"message" : "UpdatedSuccessfully"})
    return JsonResponse({"Error" : "PUT method only"})