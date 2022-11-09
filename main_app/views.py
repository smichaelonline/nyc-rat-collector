from django.shortcuts import render
from .models import Rat 

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request): 
  return render(request, 'about.html')

def rats_index(request): 
  rats = Rat.objects.all()
  return render(request, 'rats/index.html', {'rats': rats })

def rats_detail(request, rat_id):
  rat = Rat.objects.get(id=rat_id)
  return render(request, 'rats/detail.html', {'rat': rat}) 