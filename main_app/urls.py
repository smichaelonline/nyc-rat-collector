from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('rats/', views.rats_index, name='rats_index'),
  path('rats/<int:rat_id>/', views.rats_detail, name='rats_detail'),
  path('rats/create/', views.RatCreate.as_view(), name='rats_create'),
  path('rats/<int:pk>/update/', views.RatUpdate.as_view(), name='rats_update'),
  path('rats/<int:pk>/delete/', views.RatDelete.as_view(), name='rats_delete'),
  path('rats/<int:rat_id>/add_feeding/', views.add_feeding,name='add_feeding'),
]