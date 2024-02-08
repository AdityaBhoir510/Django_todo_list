from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from .models import guest
from datetime import datetime

# Create your views here.
class login(View):
    def get(self,request):
        return render(request,"login.html")
    
class register(View):
    def get(self,request):
        return render(request,"register.html")

class todo(View):
    
    def get(self,request):
        context ={}
        v=guest.objects.all()
        context['data']=v
        # print(context['data'])
        return render(request,"todo.html",context)
    
    def post(self,request):
        task = request.POST['task']
        # print(task)
        c = guest.objects.create(task=task)
        c.save()

        return redirect('/todo')
        # return HttpResponse("task saved")
    
    # ------delete task---------
class delete(View):
    def get(self,request,id):
        d = guest.objects.get(id=id)
        print(d)
        d.delete()
        
        return redirect('/todo')
        # return HttpResponse("delete page "+id)
    
    # --------edit---------
class edit(View):
    def get(self,request,eid):
        context ={}
        v=guest.objects.all()
        context['data']=v
        context['editid']=eid
        print(context['data'])
        print(context['data'][0].task)
        return render(request,"edit.html",context)

    def post(self,request,eid):
        task = request.POST['task']
        # print(task)
        u = guest.objects.filter(id=eid)
        u.update(id=eid,task=task)
        # c.save()
        
        return redirect('/todo') 