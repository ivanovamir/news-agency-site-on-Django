from . import views
from django.urls import URLPattern, path
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('/register', views.RegisterUser.as_view(), name='register'),
    path('/login', views.LoginUser.as_view(), name='login'),
    path('/logout', views.logoutUser, name='logout'),
    path('/contact', views.ContactFormView.as_view(), name='contact'),

    path('', cache_page(60)(views.Home.as_view()), name='home'), #cache 60 seconds
    path('<slug:slug_new>/', views.New.as_view(), name='show_new'),
    path('tag/<slug:slug_tag>', cache_page(60)(views.Show_tag.as_view()), name='show_tag'), #cache 60 seconds
    path('<slug:slug_new>/review>/', views.ReviewView.as_view(), name='review'),
    

]