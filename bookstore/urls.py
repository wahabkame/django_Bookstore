from django.urls import path
from . import views
 
urlpatterns = [  
  path('',views.home,name="home"),
  path('books/',views.books,name="books"),
  #path('customer/',views.customer),
  path('customer/<str:pk>',views.customer,name="customer"),
  #path('create/',views.create,name="create"),
  path('create/<str:pk>',views.create,name="create"),
  path('update/<str:pk>',views.update,name="update"),
  path('delete/<str:pk>',views.delete,name="delete"),

  path('register/',views.register,name="register"),
  path('login',views.userLogin,name="login"),
  path('logout',views.userLogout,name="logout"),
]