from django.shortcuts import render,HttpResponseRedirect
from .forms import studentregistration
from .models import user
def add(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            sn = fm.cleaned_data['Student_name']
            cl = fm.cleaned_data['Class']
            rl = fm.cleaned_data['roll_no']
            reg = user(Student_name = sn , Class = cl, roll_no = rl)
            reg.save()
            fm = studentregistration()
    else:
        fm = studentregistration()
    return render(request,'add.html',{'form':fm})


def show(request):
    stds = user.objects.all()
    context = {
        'std':stds
    }
    return render(request,'show.html',context)

def delete(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/show')

def update(request,id):
    if request.method == 'POST':
        pi = user.objects.get(pk=id)
        fm = studentregistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            
    else:
        pi = user.objects.get(pk=id)
        fm = studentregistration(instance=pi)
    return render(request,'update.html',{'form':fm})
