from django.contrib.auth import views
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic import RedirectView
from rest_auth.views import LoginView

from apps import settings
from contas.views.conta import ContaAPIView, FormContaAPIView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('accounts/profile/', RedirectView.as_view(url='/lista/')),

    path('formulario/', FormContaAPIView.as_view(), name='formulario'),
    path('lista/?<str:ordering>', ContaAPIView.as_view()),
    path('lista/', ContaAPIView.as_view(), name='lista'),
    path('autenticacao/', LoginView.as_view(), name='autenticacao'),
    path('', views.LoginView.as_view(template_name='rest_framework/login.html')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
