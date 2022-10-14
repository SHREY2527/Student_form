from django.urls import path
from . import views

urlpatterns = [
    path('',views.add),
    path('show',views.show,name ='show'),
    path('delete/<int:id>/',views.delete,name = 'delete_data'),
    path('<int:id>/',views.update,name='update_data'),
    
]
