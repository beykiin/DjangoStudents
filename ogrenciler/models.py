from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ogrenciler(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    resim=models.FileField(upload_to="ogrenciResim",verbose_name="Öğrenci Fotoğrafı: ")
    isim=models.CharField(max_length=100, verbose_name="Öğrenci Adı: ")
    soyad=models.CharField(max_length=100,verbose_name="Öğrenci Soyad: ")
    hakkinda=models.TextField(max_length=500,verbose_name="Öğrenci Hakkında: ")
    def __str__(self):
        return self.isim +" "+ self.soyad
    