from django.db import models
import uuid
from user.models import UserModel 
import datetime

class Image(models.Model):
    path = models.CharField(max_length=255, default="")  
    name = models.CharField(max_length=255, default="") 

    def __str__(self):
        return self.name or "Không có ảnh"


class EventModel(models.Model):
    
    id = models.UUIDField( default=uuid.uuid4,primary_key=True, editable=False)  
    title = models.CharField(max_length=255) 
    description = models.TextField(default="") 
    max_people = models.IntegerField(default=0)  
    start_time =models.DateField(default=datetime.date.today )
    end_time =models.DateField(default=datetime.date.today)
    
    images = models.ManyToManyField(    Image, related_name="events", blank=True  )

    all_user_registed = models.ManyToManyField(      UserModel, related_name="registered_events", blank=True
    )
    def check_event_is_expire(self):
        return datetime.date.today()> self.end_time
    def __str__(self):
        return self.title
    def so_nguoi_tham_gia_hien_tai(self):
        return self.all_user_registed.count
    def them_nguoi_tham_gia(self,user):
        self.all_user_registed.add(user)
