from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Rat, Trait 
from .forms import FeedingForm

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
  traits_rat_doesnt_have = Trait.objects.exclude(id__in = rat.traits.all().values_list('id'))
  feeding_form=FeedingForm()
  return render(request, 'rats/detail.html', {'rat': rat, 'feeding_form': feeding_form, 'traits': traits_rat_doesnt_have}) 

def add_feeding(request, rat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.rat_id = rat_id 
    new_feeding.save() 
  return redirect('rats_detail', rat_id=rat_id)

def assoc_trait(request, rat_id, trait_id):
  Rat.objects.get(id=rat_id).traits.add(trait_id)
  return redirect('rats_detail', rat_id=rat_id)

class RatCreate(CreateView):
  model = Rat 
  fields = ['name', 'color', 'description', 'location']
  success_url= '/rats/'

class RatUpdate(UpdateView):
  model = Rat
  fields = ['color', 'description', 'location']

class RatDelete(DeleteView):
  model = Rat
  success_url= '/rats/'

class TraitCreate(CreateView):
  model = Trait
  fields='__all__'

class TraitList(ListView):
  model = Trait

class TraitDetail(DetailView):
  model = Trait

class TraitUpdate(UpdateView):
  model = Trait
  fields = ['name', 'color']

class TraitDelete(DeleteView):
  model = Trait
  success_url = '/traits/'

