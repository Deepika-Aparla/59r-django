from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

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