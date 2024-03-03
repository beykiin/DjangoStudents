from django.contrib.auth.models import User

def getAllContext(request):
    kullanicilar=User.objects.all()
    context={
        "kullanicilar":kullanicilar
    }
    return context