from django.urls import path,include
from . import views

urlpatterns = [
    path('register', views.register , name='register'),
    path('login', views.login , name='login'),
    path('home',views.home,name='home'),
    path('addtask',views.addTask,name='addTask'),
    path('delete/<taskid>',views.deleteTask,name='deleteTask'),
    path('update/<taskid>', views.updateTask),
    path('update/update/<taskid>', views.updateTask),
    path('logout',views.logout),
]
