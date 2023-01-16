from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
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

    if request.method == 'POST':
        form = PostFormAddFunctionAndSection(request.POST)
        if form.is_valid():
            return redirect('compiler')
        else:
            return redirect('laboratory')
    else:
        form = PostFormAddFunctionAndSection()

    context = {
        'posts': posts,
        'laboratory': laboratory,
        'form': form,
    }

    return render(request, 'dip/post_laboratory.html', context=context)


def compiler(request):
    posts = Lecture.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'dip/compiler.html', context=context)

# def show_page_parameters_and_inaccuracy(request):
#     posts = Lecture.objects.all()
#
#     if request.method == 'POST':
#         form = FormParametersAndInaccuracy(request.POST)
#         if form.is_valid():
#             return redirect('inaccuracy_and_parameters')
#         else:
#             return redirect('laboratory')
#     else:
#         form = FormParametersAndInaccuracy()
#
#     context = {
#         'posts': posts,
#         'form': form,
#     }
#
#     return render(request, 'dip/parameters_and_inaccuracy.html', context=context)