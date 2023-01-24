from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('booking',views.booking,name='booking'),
    path('doctor',views.doctors,name='doctor'),
    path('department',views.department,name='department'),
    path('contact',views.contact,name='contact'),
    path('search',views.search,name='search_u'),
]


