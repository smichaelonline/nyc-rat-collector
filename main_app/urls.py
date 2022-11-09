from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('rats/', views.rats_index, name='cats_index'),
  path('rats/<int:rat_id>/', views.rats_detail, name='rats_detail')
]