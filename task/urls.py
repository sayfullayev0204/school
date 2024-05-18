from django.urls import path
from .views import home,tek,fan,uzifa,sinf,info
urlpatterns = [
    path('', home, name='home'),
    path('sinf/', sinf, name='sinf'),
    path('tek/', tek, name='tek'),
    path('fan/', fan, name='fan'),
    path('vazifa/', uzifa, name='vazifa'),
    path('info/', info, name='info'),
]
