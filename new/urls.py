from . import views
from django.urls import URLPattern, path

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('<slug:slug_new>/', views.New.as_view(), name='show_new'),
    path('tag/<slug:slug_tag>', views.Show_tag.as_view(), name='show_tag'),
    path('<slug:slug_new>/review>/', views.ReviewView.as_view(), name='review'),
    # path('login/', views.login, name='login'),
    # path('register/', views.RegisterUser.as_view(), name='register'),
]