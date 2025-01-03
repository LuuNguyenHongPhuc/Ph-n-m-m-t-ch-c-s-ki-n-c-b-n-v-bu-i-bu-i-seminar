from django.shortcuts import render
from django.views import View
from app.util import get_current_user

class AdminPanel(View):
    template_link = "admin/admin.html"

    def get(self, request):
        now_user =get_current_user(request=request)
        print(now_user)
        auth =now_user is None
        context ={
            'admin':now_user,
            

        }
        return render(request, self.template_link,context)


class UserPanel(View):
    template_link ="user/user.html"