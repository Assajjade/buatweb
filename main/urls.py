from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main),
    path('panduan/', show_Panduan),
    path('lokal/', form),
    path('pr/', show_Pr),
    path('primary/', show_Primary),
    path('sec/', show_Sec),
]

