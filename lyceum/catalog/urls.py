from django.urls import path, re_path

from . import views

app_name = 'catalog'

urlpatterns = [
    # Домашнаяя дириктория приложения catalog
    path('', views.item_list, name='item_list'),

    # Целое положительное число большее 0
    re_path(r'^(?P<pk>[1-9]*)/$', views.item_detail, name='item_detail'),
]
