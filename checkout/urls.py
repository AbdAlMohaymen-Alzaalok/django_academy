from django.urls import path
from . import views

urlpatterns = [
path('order/<int:cid>/',views.make_order,name='order'),
path('my_courses/',views.my_courses,name='my_courses'),
]
