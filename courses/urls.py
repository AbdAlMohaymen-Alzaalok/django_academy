from django.urls import path
from . import views
urlpatterns = [
path('',views.index,name='index'),
path('course/<int:cid>/',views.course,name='course'),
path('checkout/<int:cid>/',views.checkout,name='checkout'),
path('wrong/<int:cid>/',views.wrong,name='wrong'),
path('right/<int:cid>/',views.right,name='right'),
path('course/<int:cid>/comment/',views.add_comment,name='comment'),
path('reply/<int:cmid>/',views.add_reply,name='reply'),
]
