from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'main'

urlpatterns = [
    path('', views.main,name='main'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('sign_out', views.sign_out, name='sign_out'),
    path('sign_search', views.sign_search, name='sign_search'),
    path('sign_search_id', views.sign_search_id, name='sign_search_id'),
    path('sign_search_password', views.sign_search_password, name='sign_search_password'),
    path('sign_search_id_page', views.sign_search_id_page, name='sign_search_id_page'),
    path('sign_search_password_page', views.sign_search_password_page, name='sign_search_password_page'),
    path('search', views.search, name='search'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)