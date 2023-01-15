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
    posts = Lecture.objects.all()

    context = {
        'posts': posts,
        'lecture': lecture,
        'title': lecture.title,
    }

    return render(request, 'dip/post_lecture.html', context=context)


def show_laboratory(request, laboratory_id):
    laboratory = get_object_or_404(Lecture, pk=laboratory_id)
    posts = Lecture.objects.all()

    context = {
        'posts': posts,
        'laboratory': laboratory,
    }

    return render(request, 'dip/post_laboratory.html', context=context)

# def show_category(request):
#     category = Lecture.objects.all()
#
#     context = {
#         'category': category,
#         'title': 'Лекции',
#     }
#
#     return render(request, 'dip/index.html', context=context)
