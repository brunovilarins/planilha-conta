from django.contrib import admin
from django.urls import path, include

from contas.views.conta import ContaAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('?<str:ordering>', ContaAPIView.as_view()),
    path('', ContaAPIView.as_view()),



]
