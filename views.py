from django.shortcuts import render

def index(request):
       return render(request, 'page1/index.html') 

def firstpage(request):
     return render(request, 'page1/firstpage.html') 
       
def secoundpage(request):
      return render(request, 'page1/secoundpage.html') 

