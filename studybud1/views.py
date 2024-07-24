from django.http import HttpResponse ,HttpResponseRedirect
from django.shortcuts import render
from .forms import usersform
from news.models import News
from service.models  import Service
from django.core.mail import send_mail
from media.forms import ImageForm
from media.models import UploadImage  


def HOME(request):
    
#     send_mail(
#     "Subject here",
#     "HELLO MA'AM  Welcom Guider_space. This mail come from automated",
#     "ce22b001@iittp.ac.in",
#     ["adarshkum3212@gmail.com"],
#     fail_silently=False,
# )
    newsdata= News.objects.all()
    servicesData = Service.objects.all()
    for a in  servicesData:
        print(a)
        
    print(Service)    
    data= {
        'servicesData': servicesData,
        'newsdata':newsdata
    }
    return render(request,"main.html",data)
def newsDetail(request,slug):
    newsdetails=News.objects.get(news_slug=slug)
    data = {
        'newsdetails':newsdetails
    }
    return render (request,"about_us.html",data)


def aboutus(request):  
    if request.method == 'GET' :
        output= request.GET.get('output')
    return render (request,"about_us.html",{'output': output})

def userform(request):
    finalans=0
    fn= usersform()
    data = {'form': fn }
    try:
        if request.method == 'POST':
         n1=int(request.POST.get('num1'))
         n2=int(request.POST.get('num2'))
         finalans=(n1+n2)
         data = {
            #  'n1': n1 ,
            #  'n2':n2 ,
             'form': fn,
             'output':finalans ,
         }
         url=  "/aboutus/?output={}".format(finalans)
         return HttpResponseRedirect(url)
    except:
        pass    
    return render (request,"userform.html",data)

def course(request):
    return HttpResponse ("welcome to adarshwadi world1")

def coursed(request, courseId):
    return HttpResponse(courseId)

def submitform(request):
    return HttpResponse(request)


def image_request(request):  
    if request.method == 'POST':  
        form = ImageForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save()  
  
            # Getting the current instance object to display in the template  
            img_object = form.instance  
              
            return render(request, 'prev.html', {'form': form, 'img_obj': img_object})  
    else:  
        form = ImageForm()  
  
    return render(request, 'prev.html', {'form': form}) 

def calculater(request):
    c =' '
    try:
        if request.method == 'POST' :
            n1=eval(request.POST.get('num1'))
            n2=eval(request.POST.get('num2'))
            opr=(request.POST.get('opr'))
            if opr == "+":
                c= n1+n2
            elif  opr == "-":
                c= n1- n2  
            elif  opr == "*":
                c= n1*n2  
            elif  opr == "/":
                 c= n1/n2  
    except:
        pass   
    print(c)  
    return render(request ,"calculater.html",{'c': c})        
     