from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Studentdetail
from .forms import studentform

def index(request):
    return render(request,'index.html')

def form(request):
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

def form_list(request):
    stds = Studentdetail.objects.all()
    context = {
        'stds':stds
    }
    return render(request,'form_list.html',context)

def student_delete(request,id):
    if request.method == 'POST':
        stds = Studentdetail.objects.get(pk=id)
        stds.delete()
        return HttpResponseRedirect('/form_list/')
def edit_detail(request,id):
        stds = Studentdetail.objects.get(id=id)
        return render(request,'update.html',{'std':stds})

def update_detail(request,id):
        stup = Studentdetail.objects.get(id=id)         
        form = studentform(request.POST,instance=stup)
        if form.is_valid():
            form.save()
            return render(request,'update.html',{'std':stup})
            



