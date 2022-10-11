from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('form/',views.form),
    path('succesview/',views.form),
    path('form_list/',views.form_list),
   
]
