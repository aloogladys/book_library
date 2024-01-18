from django.urls import path
from . import views 

urlpatterns = [
    path('',views.getData),
    path('add/',views.addBook),
    path('single/<id>',views.getoneData),
    path('delete/<id>',views.deleteBook),
    path('update/<id>',views.updateBook)


]