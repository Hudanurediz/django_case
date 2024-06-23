

from django.urls import path

from . import views
urlpatterns=[
  path('',views.login),
  path('login/', views.login, name='login'),
  path('register/', views.register, name='register'),
  path('logout/', views.logout, name='logout'),
  path('iha-features/', views.getAndSaveIhaFeatures, name='iha-features'),
  path('iha-features/view/', views.ihafeatures_view, name='iha-features-view'),

]