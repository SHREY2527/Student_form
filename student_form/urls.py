from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('form/',views.form, name='form'),
    path('succesview/',views.form, name='succesview'),
    path('form_list/',views.form_list, name='form_list'),
    path('delete/<int:id>/',views.student_delete, name = 'student_delete'),
    path('edit/<int:id>/',views.edit_detail, name = "edit_detail"),
    path('<int:id>/',views.update_detail, name = 'update_detail'),
]
