from django.urls import path, re_path

from . import views

app_name = 'catalog'

urlpatterns = [
    # Домашнаяя дириктория приложения catalog
    path('', views.ItemList.as_view(), name='item_list'),

    # Целое положительное число большее 0
    re_path(r'^(?P<pk>[1-9][0-9]*)/$', views.ItemDetail.as_view(),
            name='item_detail'),
]
