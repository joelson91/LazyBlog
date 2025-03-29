from django.urls import path
from core import views as core_views

urlpatterns = [
    path('<slug:slug>/', core_views.post, name='post'),
]