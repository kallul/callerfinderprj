from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('auth/token',views.truecaller,name = "truecaller"),    
    path('ajaxpost', views.ajaxpost,name = "ajaxpost"),
    path('search_phone', views.search_phone,name = "search"),
]
