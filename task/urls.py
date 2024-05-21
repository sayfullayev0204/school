from django.urls import path
from .views import home,tek,fan,uzifa,sinf,info
from .views import SelectClass
urlpatterns = [
    path('', home, name='home'),
    path('sinf/', SelectClass.as_view(), name='sinf'),
    path('tek/', tek, name='tek'),
    path('fan/', fan, name='fan'),
    path('vazifa/', uzifa, name='vazifa'),
    path('info/', info, name='info'),
]
