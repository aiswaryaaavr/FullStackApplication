from django.urls import path
from .import views

# . means from current directory import gvn
urlpatterns = [
   
    path('register/',views.reg,name='register/'),
    path('login/',views.login,name='login'),     
    path('get/',views.get_data,name='get/'),
    path('del/',views.delete_data,name='del/'),
    path('put/',views.update_data,name='put/')

    ]
# when user registers , go to views  , to go only it is imported