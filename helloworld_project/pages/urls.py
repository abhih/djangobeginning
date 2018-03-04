from django.urls import path
from . import views
urlpatterns=[
    path('',views.homePageView.as_view(),name='home'),
    path('about/',views.aboutPageView.as_view(),name='about'),
    path('admin/',views.adminPageView.as_view(),name='adminPage'),

]