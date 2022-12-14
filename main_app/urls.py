from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('rats/', views.rats_index, name='rats_index'),
  path('rats/<int:rat_id>/', views.rats_detail, name='rats_detail'),
  path('rats/create/', views.RatCreate.as_view(), name='rats_create'),
  path('rats/<int:pk>/update/', views.RatUpdate.as_view(), name='rats_update'),
  path('rats/<int:pk>/delete/', views.RatDelete.as_view(), name='rats_delete'),
  path('rats/<int:rat_id>/add_feeding/', views.add_feeding,name='add_feeding'),
  path('rats/<int:rat_id>/assoc_trait/<int:trait_id>/', views.assoc_trait, name='assoc_trait'),
  path('traits/create/', views.TraitCreate.as_view(), name='traits_create'),
  path('traits/<int:pk>/', views.TraitDetail.as_view(), name='traits_detail'),
  path('traits/', views.TraitList.as_view(), name='traits_index'),
  path('traits/<int:pk>/update/', views.TraitUpdate.as_view(), name='traits_update'),
  path('traits/<int:pk>/delete/', views.TraitDelete.as_view(), name='traits_delete'),
  path('accounts/signup/', views.signup, name='signup'),
]