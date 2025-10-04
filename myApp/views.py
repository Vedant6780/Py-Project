from django.shortcuts import render,HttpResponse
from myApp.models import Contact

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'About.html')

    # return HttpResponse("this is about page")

def services(request):
    return render(request,'service.html')

    # return HttpResponse("this is service page")

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        feedback = request.POST.get("feedback")
        contact_obj=Contact(name=name,email=email,phone=phone,feedback=feedback)
        contact_obj.save()
        
    return render(request, 'contact.html')


    # return HttpResponse("this is contact page")
