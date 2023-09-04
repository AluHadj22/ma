from django.shortcuts import render

def home(request):
   return render(request, 'filemarya/home.html')