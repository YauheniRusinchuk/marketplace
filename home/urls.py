from django.urls import path
from home.views import index, DetailPost
from django.views.generic import TemplateView

app_name = 'home'

urlpatterns = [
    path('', index, name='index_page'),
    path('announcement/<int:pk>', DetailPost.as_view(), name='index_detail'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='index_about')
]
