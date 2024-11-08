# meu_projetoloja/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from loja.views import RegisterView  # Supondo que a view de registro estará em loja.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('loja.urls')),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),  # URL para a view de registro
]

