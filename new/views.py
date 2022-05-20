from email import message
from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404

from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect

from django.views.generic import View, ListView, CreateView
from django.views.generic.edit import FormView
from django.core.paginator import Paginator
from django.core.cache import cache
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

from .forms import *
from .models import *
from .utils import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'new/register.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'new/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_success_url(self):
        return reverse_lazy('home')


def logoutUser(request):
    logout(request)
    return redirect('login')


class Home(ListView): 

    paginate_by = 3 #Pagination by 3 post in a page, u can change it. I did that cus i have a little bit news)

    model = News
    template_name = 'new/home.html'
    context_object_name = 'news' 
    # success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
        
    def get_queryset(self):
        return News.objects.filter(is_published=True)


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'new/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class New(View):
    def get(self, request, slug_new, *args, **kwargs):
        new = get_object_or_404(News, slug=slug_new)
        reviews = Review.objects.filter(news=new)
        reviews_cache_update_recently = cache.get('reviews')
        if not reviews_cache_update_recently:
            reviews = Review.objects.filter(news=new)
            cache.set('reviews_cache_update_recently', reviews_cache_update_recently, 60)
        ip = get_client_ip(request)
        if Ip.objects.filter(ip=ip).exists():
            new.ip.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            new.ip.add(Ip.objects.get(ip=ip))
        
        context = {'new':new, 'reviews':reviews}
        return render (request, 'new/show_new.html', context)


class Show_tag(View):
    def get(self, request, slug_tag, *args, **kwargs):
        tag_name = Tag.objects.get(name=slug_tag)
        news = News.objects.filter(tags=tag_name)
        context = {'tag_name':tag_name, 'news':news}
        return render (request, 'new/list_news.html', context)


class ReviewView(View):
    
    def post(self, request, slug_new):
        new = News.objects.get(slug=slug_new)
        review_body = request.POST['review']
        review = Review(body=review_body, news=new)
        review.save()
        return redirect (request.META.get('HTTP_REFERER'))
        

#Unique Viusitors func
#if you expand the site, then each user will have a unique ip, which will be entered into the database and the counter of unique views will be updated
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1] #chaacking proxy servers, cus the real IP is usually at the end of the list
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip

    




    


