from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request): 
  return render(request, 'about.html')

class Rat: 
  def __init__(self, name, color, description, location): 
    self.name = name
    self.color = color
    self.description = description
    self.location = location 

rats = [
  Rat('Splinter', 'black', 'Hangs out in the subway', 'Times Square'),
  Rat('Pizza Rat', 'grey', 'found some pizza boii', '3rd Ave Subway Station'),
  Rat('Feral Rat', 'spots', 'screams at pedestrians', 'the street'),
]

def rats_index(request): 
  return render(request, 'rats/index.html', {'rats': rats })