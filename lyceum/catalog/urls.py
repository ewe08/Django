from django.urls import path, re_path

from . import views

urlpatterns = [
    # Домашнаяя дириктория приложения catalog
    path('', views.item_list),

    # Целое положительное число большее 0
    re_path(r'^(?P<pk>[1-9][0-9]*)/$', views.item_detail),
]
