from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team
# Create your views here.
def demo1(request):
   obj=Place.objects.all()
   obj2 =Team.objects.all()
   # return HttpResponse("hello abin")
   # name="india"
   return render(request,"index.html",{'result':obj,'result2':obj2})
# def about(request):
#    return render(request,"about.html")
# def addition(request):
#      x=int(request.GET['num1'])
#      y=int(request.GET['num2'])
#      res=x+y
#      return render(request, "result.html",{'resl':res})