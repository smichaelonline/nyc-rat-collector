from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Rat, Trait 
from .forms import FeedingForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request): 
  return render(request, 'about.html')

@login_required
def rats_index(request): 
  rats = Rat.objects.filter(user=request.user)
  return render(request, 'rats/index.html', {'rats': rats })

@login_required
def rats_detail(request, rat_id):
  rat = Rat.objects.get(id=rat_id)
  traits_rat_doesnt_have = Trait.objects.exclude(id__in = rat.traits.all().values_list('id'))
  feeding_form=FeedingForm()
  return render(request, 'rats/detail.html', {'rat': rat, 'feeding_form': feeding_form, 'traits': traits_rat_doesnt_have}) 

@login_required
def add_feeding(request, rat_id):
  form = FeedingForm(request.POST)
  if form.is_valid():
    new_feeding = form.save(commit=False)
    new_feeding.rat_id = rat_id 
    new_feeding.save() 
  return redirect('rats_detail', rat_id=rat_id)

@login_required
def assoc_trait(request, rat_id, trait_id):
  Rat.objects.get(id=rat_id).traits.add(trait_id)
  return redirect('rats_detail', rat_id=rat_id)

class RatCreate(LoginRequiredMixin, CreateView):
  model = Rat 
  fields = ['name', 'color', 'description', 'location']
  success_url= '/rats/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class RatUpdate(LoginRequiredMixin, UpdateView):
  model = Rat
  fields = ['color', 'description', 'location']

class RatDelete(LoginRequiredMixin, DeleteView):
  model = Rat
  success_url= '/rats/'

class TraitCreate(LoginRequiredMixin, CreateView):
  model = Trait
  fields='__all__'

class TraitList(LoginRequiredMixin, ListView):
  model = Trait

class TraitDetail(LoginRequiredMixin, DetailView):
  model = Trait

class TraitUpdate(LoginRequiredMixin, UpdateView):
  model = Trait
  fields = ['name', 'color']

class TraitDelete(LoginRequiredMixin,DeleteView):
  model = Trait
  success_url = '/traits/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('rats_index')
    else: 
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
