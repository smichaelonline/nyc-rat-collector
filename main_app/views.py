from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class RatCreate(CreateView):
  model = Rat 
  fields = '__all__'
  success_url= '/rats/'

class RatUpdate(UpdateView):
  model = Rat
  fields = ['color', 'description', 'location']

class RatDelete(DeleteView):
  model = Rat
  success_url= '/rats/'