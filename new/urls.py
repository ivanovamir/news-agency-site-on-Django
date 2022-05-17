from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.Home, name='home'),
    path('<slug:slug_new>/', views.show_new, name='show_new'),
    path('tag/<slug:slug_tag>', views.show_tag, name='show_tag'),
    path('<slug:slug_new>/review>/', views.review, name='review')

]