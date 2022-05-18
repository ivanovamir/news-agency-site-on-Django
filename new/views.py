from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import *
from .models import *
from .utils import *


class Home(ListView): 

    paginate_by = 1

    model = News
    template_name = 'new/home.html'
    context_object_name = 'news' 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


class New(View):
    def get(self, request, slug_new, *args, **kwargs):
        new = get_object_or_404(News, slug=slug_new)
        reviews = Review.objects.filter(news=new)
        ip = get_client_ip(request)
        if Ip.objects.filter(ip=ip).exists():
            new.views.add(Ip.objects.get(ip=ip))
        else:
            Ip.objects.create(ip=ip)
            new.views.add(Ip.objects.get(ip=ip)) 
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
        # if request.method == 'POST':
        #     form = AddReviewForm(request.POST)
        #     if form.is_valid():
                
        #         try:
        #             Review.objects.create(**form.cleaned_data)
        #         except:
        #             form.add_error(None, 'Error with review posting')
        # else:
        #     form = AddReviewForm()
        # return redirect (request.META.get('HTTP_REFERER'))

# class RegisterUser(CreateView):
#     # form_class = UserCreationForm
#     # success_url = reverse_lazy('login')
#     # template_name = 'new/register.html'

#     # def register_user(self, request, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     c_def = self.get_user_context(title='Registration')
#     #     return dict(list(context.items()) + list(c_def.items()))
#     pass

# def login(request):
#     pass


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR') # В REMOTE_ADDR значение айпи пользователя
    return ip