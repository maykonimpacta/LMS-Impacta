"""gestao_escolar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('cursos.html', TemplateView.as_view(template_name='cursos.html'), name='cursos'),
    path('noticias.html', TemplateView.as_view(template_name='noticias.html'), name='noticias'),
    path('curso-ads.html', TemplateView.as_view(template_name='curso-ads.html'), name='curso_ads'),
    path('curso-prodmidia.html', TemplateView.as_view(template_name='curso-prodmidia.html'), name='curso_prodmidia'),
    path('curso-si.html', TemplateView.as_view(template_name='curso-si.html'), name='curso_si'),
    path('curso-bd.html', TemplateView.as_view(template_name='curso-bd.html'), name='curso_bd'),
    path('curso-gestti.html', TemplateView.as_view(template_name='curso-gestti.html'), name='curso_gestti'),
    path('n-5vantagens.html', TemplateView.as_view(template_name='n-5vantagens.html'), name='n_5vantagens'),
    path('n-marketingdigital.html', TemplateView.as_view(template_name='n-marketingdigital.html'), name='n_marketingdigital'),
    path('n-filmes.html', TemplateView.as_view(template_name='n-filmes.html'), name='n_filmes'),
    path('n-engsoftware.html', TemplateView.as_view(template_name='n-engsoftware.html'), name='n_engsoftware'),
    path('diciplina-ads.html', TemplateView.as_view(template_name='diciplina-ads.html'), name='diciplina_ads'),
    path('diciplina-bd.html', TemplateView.as_view(template_name='diciplina-bd.html'), name='diciplina_bd'),
    path('diciplina-gestti.html', TemplateView.as_view(template_name='diciplina-gestti.html'), name='diciplina_gestti'),
    path('diciplina-prodmidia.html', TemplateView.as_view(template_name='diciplina-prodmidia.html'), name='diciplina_prodmidia'),
    path('diciplina-si.html', TemplateView.as_view(template_name='diciplina-si.html'), name='diciplina_si'),
    path('professores.html', TemplateView.as_view(template_name='professores.html'), name='professores'),
    path('notas.html', TemplateView.as_view(template_name='notas.html'), name='notas'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
