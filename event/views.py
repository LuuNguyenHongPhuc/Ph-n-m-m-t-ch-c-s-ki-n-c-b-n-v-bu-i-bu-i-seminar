from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .forms import CreateEventForm
from .models import EventModel
from app.util import get_current_user
class CreateEvent(View):
    def get(self, request):
        form = CreateEventForm()
        return render(request, "create.html", {'form': form})

    def post(self, request):
        form = CreateEventForm(request.POST)
        if form.is_valid():
            new_event = form.save()
            messages.success(request, "Tạo event mới thành công")
            return redirect("/event/list")
        else:
            print(form.errors)
            return render(request, "create.html", {'form': form})


class ListEvent(View):
    
    def get(self,request):
        all_event =EventModel.objects.all()
        return render(request,"list.html",{'list':all_event})
    
class Event(View):
    
    def get(self,request,id_event):
        user =get_current_user(request)
        print("nguoi dung yeu cau lay thong tin event co id la"+id_event)
        find_event =EventModel.objects.filter(id=id_event).first()
        print(find_event.all_user_registed.count())
        return render(request,"event.html",{"event":find_event,"auth":user,'now_people':find_event.all_user_registed.count()})
    def post(self,request,id_event):
        user =get_current_user(request)
        find_event =EventModel.objects.filter(id=id_event).first()
        if user is not None:
            
            find_event.them_nguoi_tham_gia(user)

            print(find_event.all_user_registed.count())
            
        else:
            print("người dù(ng chưa đăng nhập không thực hiện chức ăng được")
            
        return render(request,"event.html",{'event':find_event, 'auth':user,'now_people':find_event.all_user_registed.count()})
        
