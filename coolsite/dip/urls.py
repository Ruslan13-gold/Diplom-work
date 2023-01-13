from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('lecture/<int:lecture_id>/', show_lecture, name='lecture')
]
