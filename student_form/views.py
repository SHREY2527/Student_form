from django.http import HttpResponse
from django.shortcuts import render
from .models import Studentdetail

def new_page(request):
    if request.method == "POST":
        sn = request.POST['sname']
        cl = request.POST['class']
        rl = request.POST['roll_no']
        o_ref =Studentdetail(Student_name=sn,Class=cl,roll_no=rl)
        o_ref.save()
        return render (request,'succesview.html',{'message':'submitted'})
    elif request.method == 'GET':
        return render(request,'form.html')
    else:
        return HttpResponse('error')


    

    
       
