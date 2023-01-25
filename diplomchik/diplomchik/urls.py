"""diplomchik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, re_path
from manuals import views
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls import include
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    re_path(r'^coffins/', views.coffins, name="coffins"),  # маршрут по умолчанию
    re_path(r'^article_desc/(?P<article_id>\d+)/', views.article_descr, name="article_descr"),
    # венки
    re_path(r'^crown/$', views.crown, name="crown"),  # маршрут по умолчанию
    #re_path(r'^crown/(?P<article_id>\d+)/', views.article_descr, name="crown"),
    # памятники
    re_path(r'^monuments/$', views.monuments, name="monuments"),  # маршрут по умолчанию
    #re_path(r'^monuments/(?P<article_id>\d+)/', views.monuments, name="monuments"),
    path('contacts/', views.contacts, name="contacts"),
    path('accounts/', include('django.contrib.auth.urls')),  # маршрут работы с пользователями
    path('accounts/registration', views.registration, name='registration'),  # маршрут для регистрации

    # Регистрация пользователей
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registration',views.registration, name='registration'),  # маршрут для регистрации

    # Скрыть товар
    re_path(r'^hidden/(?P<article_id>\d+)/',views.hidden, name="hidden" ),


    # для корзины
    # url(r'^admin/', include(admin.site.urls)),
    #re_path(r'^cart/', include('cart.urls' )), #namespace='cart'
    #re_path(r'^', include('diplomchik.urls')), #namespace='diplomchik'






]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
