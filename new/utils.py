from django.db.models import Count

from .models import *

# class DataMixin:
#     paginate_by = 1
#     def get_user_context(self, **kwargs):
#         context = kwargs
#         news = News.objects.all()
#         context['news'] = news
#         return context