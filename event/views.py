from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import View
from django.http import HttpResponse
from .forms import CreateEventForm,EditEventForm
from .models import EventModel
from app.util import get_current_user
import qrcode
##hàm tiện ích tạo qr code
def make_qr_code(body):
    body = body.encode('utf-8') 
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,)
    qr.add_data(body,optimize=0)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    response = HttpResponse(content_type="image/png; charset=utf-8")
    img.save(response, "PNG")
    return response

##
class CreateEvent(View):
    def get(self, request):
        form = CreateEventForm()
        return render(request, "create.html", {'form': form})

    def post(self, request):
        form = CreateEventForm(request.POST,request.FILES)
        if form.is_valid():
            new_event = form.save()
            text =form.cleaned_data.get("description")
            print(text)
            thumb =form.cleaned_data.get("thumb")
            image1 =form.cleaned_data.get('image1')
            if thumb is not None :
                print("lấy được thumb")
            
            messages.success( "Tạo event mới thành công")
            return redirect("/event/list")
        else:
            messages.error(request,form.errors)
            messages.error(request,form.errors)
            return render(request, "create.html", {'form': form})


class ListEvent(View):
    
    def get(self,request):
        
        user =get_current_user(request=request)
        all_event =EventModel.objects.all()
        context ={
            'list':all_event,
            'user':user
        }
        return render(request,"list.html",context)
    
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
            body = f'''
            Ve tham gia su kien: {find_event.title}
            cua nguoi dung: {user.cccd}
            '''
            
            qr =make_qr_code(body=body)
            return qr

            
        else:
            messages.error('người dùng phải đăng nhập để thực hiện chức năng')
            print("người dù(ng chưa đăng nhập không thực hiện chức ăng được")
            
        return render(request,"event.html",{'event':find_event, 'auth':user,'now_people':find_event.all_user_registed.count(),'messages':messages})
        




class User_MyEvent(View):
    template ="eventdadangky.html"
    def get(self,request):
        
        user =get_current_user(request=request)
        context ={
            'user':user
        }
        if user is not None:
            events =EventModel.objects.all().filter(all_user_registed=user)
            context ={
            'user':user,
            'events':events
            }
        return render(request,self.template,context)
        

class EditEvent(View):
    template = 'editevent.html'

    def get(self, request, id_event):
        context ={}
        user =get_current_user(request=request)
        if user is not None:
            find_event =EventModel.objects.filter(id=id_event).first()
            form =EditEventForm(instance=find_event)
            context ={
              'form':form
            }
        
        return render(request,self.template,context)
    def post(self,request,id_event):
        context ={}
        find_event =EventModel.objects.filter(id=id_event).first()
        if find_event :
            form =EditEventForm(request.POST,request.FILES,instance=find_event)
            if form.is_valid():
                print("sửa thông tin event thành công")
                form.save()
                context ={
                    'form':form
                }

        return render(request,self.template,context)
    



        
