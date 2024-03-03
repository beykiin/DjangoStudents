from django.forms import ModelForm
from .models import *

class OgrenciForm(ModelForm):
    class Meta:
        model=Ogrenciler
        fields=["isim","soyad","hakkinda","resim"]
    def __init__(self,*args,**kwargs):
        super(OgrenciForm,self).__init__(*args,**kwargs)
        self.fields["isim"].widget.attrs.update({"class":"form-control","placeholder":"Adınızı Yazınız: "})
        self.fields["soyad"].widget.attrs.update({"class":"form-control"})
        self.fields["hakkinda"].widget.attrs.update({"class":"form-control"})
        self.fields["resim"].widget.attrs.update({"class":"form-control"})
