from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import students,employees
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def view1(request):
    return HttpResponse('hello view1')
def view2(request):
    return HttpResponse('hello view2')
# json always allow object only
def view3(request):
    return JsonResponse({"status":"success","reponse":"welcome"})
def dynamicview(request):
    qp1=request.GET.get("name","world")
    return HttpResponse(f"hello {qp1}") 

# dynamicresponse using queryparameters
def movieinfo(request):
    moviename=request.GET.get("moviename","Darling")
    showtime=request.GET.get("showtime","2pm")
    ticket_cost=int(request.GET.get("ticket_cost",300))
    total_tickets=int(request.GET.get("total_tickets",4))
    total_price=ticket_cost*total_tickets
    info={"moviename":moviename,"showtime":showtime,"ticket_cost":ticket_cost,"total_tickets":total_tickets,"total_price":total_price}
    return JsonResponse({"status":"success","data":info})
def temp1(request):
    return render(request,"./simple.html")
def temp2(request):
    return render(request,"./second.html")



products = [
    {
        "name": "Wireless Mouse",
        "category": "Footwear",
        "price": 799,
        "stock": 50,
        "brand": "Logitech",
        "rating": 4.5
    },
    {
        "name": "Cotton T-Shirt",
        "category": "Fashion",
        "price": 499,
        "stock": 120,
        "brand": "Roadster",
        "rating": 4.2
    },
    {
        "name": "Bluetooth Headphones",
        "category": "Electronics",
        "price": 1999,
        "stock": 30,
        "brand": "Boat",
        "rating": 4.6
    },
    {
        "name": "Running Shoes",
        "category": "Footwear",
        "price": 2999,
        "stock": 40,
        "brand": "Nike",
        "rating": 4.5
    }
]
def productsbycategory(request,category):
    filteredData=[]
    for product in products :
        if product["category"]==category:
            filteredData.append(product)
    return JsonResponse({"status":"success","data":filteredData})


def productsbyrating(request,rating):
    rating=float(rating)
    filteredData=[]
    for product in products :
        if product["rating"]==rating:
            filteredData.append(product)
    return JsonResponse({"status":"success","data":filteredData})




def productsbyratings(request,rating):
    try:
        cnvrt_rating=float(rating)
        if request.method=="GET":
            filteredData=[]
            for product in products:
                if product["rating"]<=cnvrt_rating:
                    filteredData.append(product)
                if len(filteredData)==0:
                    msg="no products found"
                else:
                    msg="products fetched successfully"
            return JsonResponse({"status":"success","mssage":msg,"total_no_of records":len(filteredData),"data":filteredData})
        return JsonResponse({"status":"failure","message":"only get method allowed"})
    except Exception as e:
        return JsonResponse({"message":"something went wrong"})       


@csrf_exempt
def addstudent(request):
    try:
        if request.method=="POST":
            inputdata=json.loads(request.body)
            print(inputdata)
            students.objects.create(stud_name=inputdata["name"],
            stud_age=inputdata["age"],
            stud_gender=inputdata["gender"],
            stud_email=inputdata["email"])
            return JsonResponse({"status":"success","message":"record added successfully"})
        return JsonResponse({"status":"failed","message":"only post method is applied"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"})
    



@csrf_exempt
def addemployees(request):
    try:
        if request.method=="POST":
            inputdata=json.loads(request.body)
            print(inputdata)
            employees.objects.create(emp_name=inputdata["name"],
            emp_age=inputdata["age"],
            emp_gender=inputdata["gender"],
            emp_email=inputdata["email"])
            return JsonResponse({"status":"success","message":"record added successfully"})
        return JsonResponse({"status":"failed","message":"only post method is applied"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"})
    




def getstudents(request):
    try:
        if request.method=="GET":
            data=students.objects.values()
            final_result=list(data)
            print(final_result)       
            return JsonResponse({"status":"success","message":"record fetched successfully","data":final_result})
        return JsonResponse({"status":"failed","message":"only post method is applied"})
    except Exception as e:
        return JsonResponse({"status":"error","msg":"error occured"})
    
   