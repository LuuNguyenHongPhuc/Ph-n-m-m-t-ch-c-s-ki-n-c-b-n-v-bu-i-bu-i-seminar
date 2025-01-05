from django import  forms

from event.models import EventModel


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['title', 'description','thumb','image1','image2', 'max_people','start_time','end_time']

        widgets = {
            'title': forms.TextInput(attrs={"class": "title", 'placeholder': 'Nhập tên sự kiện'}),
            'description': forms.Textarea(attrs={"class": "description", 'placeholder': 'Mô tả sự kiện'}),
            'max_people': forms.NumberInput(attrs={"class": "max-user", 'placeholder': 'Số người tối đa'}),
            'start_time':forms.DateInput(attrs={"type":"date"}),
            'end_time':forms.DateInput(attrs={"type":"date"}),
        }

class GetEvent(forms.ModelForm):
    class Meta:
        model =EventModel
        fields ="__all__"

class EditEventForm(forms.ModelForm):
    class Meta:
        model =EventModel
        fields =['title','description','thumb','image1','image2', 'max_people','start_time','end_time']