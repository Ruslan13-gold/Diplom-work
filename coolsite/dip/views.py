from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404

from .models import *

menu = ['О сайте', 'Добавить статью', 'Войти']


def index(request):
    posts = Lecture.objects.all()
    return render(request, 'dip/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'dip/about.html', {'menu': menu, 'title': 'About'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_lecture(request, lecture_id):
    lecture = get_object_or_404(Lecture, pk=lecture_id)

    context = {

        'lecture': lecture,
        # 'menu': menu,
        'title': lecture.title,
    }

    return render(request, 'dip/post.html', context=context)

# def show_category(request):
#     category = Lecture.objects.all()
#
#     context = {
#         'category': category,
#         'title': 'Лекции',
#     }
#
#     return render(request, 'dip/index.html', context=context)
