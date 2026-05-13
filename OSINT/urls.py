from django.urls import path
from .views import *
from .tests import *

urlpatterns = [
    path('', index, name='index'),

    path('Open-Source-Intelligence/', osint, name='osint'),
    path('about-site/', about_site, name='about_site'),
    path('Open-Source-Intelligence/web-surfer/', web_surfer_view, name='web_surfer'),
    path('Open-Source-Intelligence/telegram/', telegram_view, name='telegram'),
    path('Open-Source-Intelligence/github/', github_view, name='github'),
]
