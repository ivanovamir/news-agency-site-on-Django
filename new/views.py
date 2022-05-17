from django.shortcuts import render
from pdb import post_mortem
from django.shortcuts import render, redirect, get_object_or_404
from matplotlib.style import context
from .models import *
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect

def Home(request):
    news = News.objects.all()
    tags = Tag.objects.all()
    context = {'news':news, 'tags':tags}
    return render (request, 'new/home.html', context)

def show_new(request, slug_new):
    new = get_object_or_404(News, slug=slug_new)
    reviews = Review.objects.filter(news=new)
    context = {'new':new, 'reviews':reviews}
    return render (request, 'new/show_new.html', context)

def show_tag(request, slug_tag):
    tag_name = Tag.objects.get(name=slug_tag)
    news = News.objects.filter(tags=tag_name)
    context = {'tag_name':tag_name, 'news':news}
    return render (request, 'new/list_news.html', context)

def review(request, slug_new):
    new = News.objects.get(slug=slug_new)
    review_body = request.POST['review']
    review = Review(body=review_body, news=new)
    review.save()
    
    return redirect (request.META.get('HTTP_REFERER'))

