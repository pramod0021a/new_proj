from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
 path('', views.index_page, name='index_name'), 
 path('signup/', views.signup_page, name='signup_name'),
 path('login/', views.login_page, name='login_name'),
 path('logout/', views.logout_page, name='logout_name'),
 path('profile/', views.profile_page, name='profile_name'),
 path('contact/', views.contact_page, name='contact_name'),
]