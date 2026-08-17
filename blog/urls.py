from django.urls import path
from . import views

urlpatterns = [
path('',views.ListBlogs.as_view(),name='list_blogs'),
path('show/<int:pk>/',views.Show_Blog.as_view(),name='show_blog'),
]
