from django.urls import path
from . import views


urlpatterns=[
    path('', views.BlogListView.as_view(), name='blog'),
    path(r'blog/<int:pk>', views.BlogDetailView.as_view(),name='blog_details_view'),
    path('new/', views.BlogCreateView.as_view(),name='blog_new'),
    path(r'blog/<int:pk>/edit', views.BlogUpdateView.as_view(),name='blog_details_edit'),
    path(r'blog/<int:pk>/delete', views.BlogDeleteView.as_view(),name='blog_details_delete'),
    
]