from django.shortcuts import render
def nativemap(request):
     return render(request,"secmap_app/nativemap.html")
def govthospital(request):
    return render(request,"secmap_app/govthospital.html") 
def policestation(request):
    return render(request,"secmap_app/policestation.html")     
def postoffice(request):
    return render(request,"secmap_app/postoffice.html") 
def school(request):
    return render(request,"secmap_app/school.html") 
def theatre(request):
    return render(request,"secmap_app/theatre.html")             