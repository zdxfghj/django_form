
from django.urls import path
from . import views

urlpatterns = [
    path('', views.forms_create, name='form_create'),
    path('view/', views.forms_view, name="form_view")
]
