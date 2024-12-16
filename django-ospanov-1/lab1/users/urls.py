from . import views
from django.urls import path


urlpatterns = [
  path('register/', views.register_view, name='list'),
  path('login/', views.login_view, name="login"),
]