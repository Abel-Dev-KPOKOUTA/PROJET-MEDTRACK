from django.shortcuts import render

def accueil(request):
    return render(request,'dashboard/dashboard.html')