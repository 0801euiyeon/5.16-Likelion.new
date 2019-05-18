from django.shortcuts import render
from .models import Hello
def home(request):
    hello = Hello.objects.all()

    return render(request,'FD/home.html', {'hello':hello})
# Create your views here.
