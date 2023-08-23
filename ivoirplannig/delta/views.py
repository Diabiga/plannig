from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    
    return render(request,"app/index.html")

def login(request):
    
    return render(request,"app/login.html")


def register(request):
    
    return render(request,"app/register.html")



def prof(request):
    
    return render(request,"app/register.html")

def groupe(request):
    
    return render(request,"app/register.html")

def matiere(request):
    
    return render(request,"app/register.html")

def cours(request):
    
    return render(request,"app/register.html")

def generer_cours(request):
    
    return render(request,"app/register.html")

def creer_cours(request):
    
    return render(request,"app/register.html")