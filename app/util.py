from user.models import UserModel

from django.contrib.auth.models import AnonymousUser

def get_current_user(request):
    if isinstance(request.user, AnonymousUser):  # Kiểm tra nếu là AnonymousUser
        print("Không có người dùng đăng nhập")
        return None
    elif request.user.is_authenticated:
        print("Có người dùng đã đăng nhập")
        return request.user
    else:
        print("Lỗi không xác định người dùng")
        return None
