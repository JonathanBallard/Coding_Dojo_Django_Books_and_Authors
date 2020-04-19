from django.urls import path 
from . import views 
 
urlpatterns = [ 
    path('', views.index), 
    path('books/<int:id>/', views.bookPage), 
    path('authors/', views.authors), 
    path('newAuthor/', views.newAuthor), 
    path('addAuthor/', views.addAuthor), 
    path('addBook/', views.addBook), 
    path('createBook/', views.createBook), 
    path('authorPage/<int:id>/', views.authorPage), 
 
] 
 
 
