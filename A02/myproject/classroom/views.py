from django.shortcuts import render
from .models import RoomData
#from django.http import HttpResponse

# Create your views here.
def index(request):
    rooms = RoomData.objects.all()
    context =  {'rooms' : rooms}
    return render(request, 'rooms/index.html', context)