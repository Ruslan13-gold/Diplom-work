from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('lecture/<int:lecture_id>/', show_lecture, name='lecture'),
    path('laboratory/<int:laboratory_id>/', show_laboratory, name='laboratory'),
    path('laboratory/compiler/', compiler, name='compiler'),
    # path('laboratory/inaccuracy_and_parameters', show_page_parameters_and_inaccuracy, name='inaccuracy_and_parameters'),
]
