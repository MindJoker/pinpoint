from django.urls import path,include
from .views import MyRegistrationView
from . import views
'''
urlpatterns = [
    path("", views.index, name="index"),
    path("master", views.master, name="master"),
    path("map", views.map, name="map"),
    path("map/<str:user>", views.map, name="map"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("sign_up", views.sign_up, name="sign_up"),
]
'''
urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in/', views.sign_in, name='sign_in'),
   # path('route_select/<int:id>/', views.route_select, name='route_select'),
    path('nav/<int:id>/', views.nav, name='nav'),
    #path('nav/<int:id>/<str:start_lat>,<str:start_long>/<str:end_lat>,<str:end_long>/', views.nav, name='nav'),
    path('accounts/register/',
         MyRegistrationView.as_view(),
         name='django_registration_register'),

]