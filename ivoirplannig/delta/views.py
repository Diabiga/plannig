from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test


@login_required
def index(request):
    
    return render(request,"app/index.html")


def login(request):
    
    return render(request,"app/login.html")

def register(request):
    
    return render(request,"app/register.html")
#admin
@login_required
#@user_passes_test()
def admin_role(request):
    
    return render(request,"app/admin/role.html")
@login_required
#@user_passes_test()
def admin_secure(request):
    
    return render(request,"app/admin/securite.html")
@login_required
#@user_passes_test()
def admin_user(request):
    
    return render(request,"app/admin/user.html")

#para
@login_required
def para_cours(request):
    
    return render(request,"app/para/para_cour.html")
@login_required
def para_groupes(request):
    
    return render(request,"app/para/para_groupe.html")

@login_required
def para_mat(request):
    
    return render(request,"app/para/para_matiere.html")
@login_required
def para_prof(request):
  
    return render(request,"app/para/para_prof.html")

#traitement 
@login_required 
def traitement_groupe(request):
    
    return render(request,"app/rlt/resultat_groupe.html")
@login_required
def traitement_matiere(request):
    
    return render(request,"app/traitement/register.html")
@login_required
def traitement_cours(request):
    
    return render(request,"app/traitement/register.html")

@login_required
def traitement_prof(request):
    
    return render(request,"app/traitement/register.html")


#rlt
@login_required
def rlt_prof(request):
    
    return render(request,"app/rlt/resulta_prof.html")
@login_required
def rlt_groupes(request):
    
    return render(request,"app/rlt/resulta_groupe.html")