from django.urls import path

from websiteApp.views import *
from . import *


urlpatterns = [
    # path('count',count,name='count'),


    path('E_login_check',login_check.as_view(),name="E_login_check"),
    path('E_login',login.as_view(),name="E_login"),


    path('',views.home,name='home'),
    path('about',views.about,name='about'),

    path('blog',views.blog,name='blog'),

    path('contact',views.contact,name='contact'),

    path('detail',views.detail,name='detail'),

    path('feature',views.feature,name='feature'),

    path('price',views.price,name='price'),

    path('quote',views.quote,name='quote'),
    path('service',views.service,name='service'),
    
    path('team',views.team,name='team'),
    path('testimonial',views.testimonial,name='testimonial'),


    
]