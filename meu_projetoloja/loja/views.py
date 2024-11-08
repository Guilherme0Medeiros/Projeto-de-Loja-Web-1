from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# View para a página inicial
class IndexView(TemplateView):
    template_name = 'index.html'

# View para registro de novos usuários
class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # Redireciona para a página de login após o registro

# LoginView personalizada, pra usar um template customizado
class CustomLoginView(LoginView):
    template_name = 'login.html'   #Template personalizado para login

# LogoutView personalizada, redirecionando para a página inicial após o logout
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')  # Redireciona para a página inicial ou outra página após logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from django.shortcuts import redirect

class CompraView(LoginRequiredMixin, View):
    login_url = 'login'  # Se o usuário não estiver logado, será redirecionado para a página de login

    def post(self, request, *args, **kwargs):
        # Lógica de compra aqui
        return redirect('compra_confirmada')
