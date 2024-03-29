from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, FormView, DetailView
from django.views import View


from .forms import *
from .models import *

menu = ['О сайте', 'Добавить статью', 'Войти']


# class MainPage(ListView):
#     model = Lecture
#     template_name = "dip/index.html"
#     context_object_name = 'posts'
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Главная страница'
#         return context
#
#     def get_queryset(self):
#         return Lecture.objects.filter(is_published=True)

def index(request):
    posts = Lecture.objects.all()
    return render(request, 'dip/index.html', {'posts': posts, 'menu': menu, 'title': 'Главная страница'})


def about(request):
    return render(request, 'dip/about.html', {'menu': menu, 'title': 'About'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_lecture(request, lecture_slug):
    posts = Lecture.objects.all()
    lecture = get_object_or_404(Lecture, slug=lecture_slug)

    context = {
        'posts': posts,
        'lecture': lecture,
        'title': lecture.title,
    }

    return render(request, 'dip/post_lecture.html', context=context)


def show_laboratory(request, laboratory_slug):
    laboratory = get_object_or_404(Lecture, slug=laboratory_slug)
    posts = Lecture.objects.all()
    form = PostFormLaboratory()
    # if request.method == 'POST':
    #     form = PostFormAddFunctionAndSection(request.POST)
    #     if form.is_valid():
    #         return redirect('home')
    #     else:
    #         return redirect('laboratory')
    # else:
    #     form = PostFormAddFunctionAndSection()

    context = {
        'posts': posts,
        'laboratory': laboratory,
        'form': form,
    }

    return render(request, 'dip/post_laboratory.html', context=context)


def laboratory_result(request):
    # laboratory = get_object_or_404(Lecture, slug=laboratory_slug)
    function = request.GET['function']

    # context = {
    #     'function_result': request.GET['function'],
    #     'laboratory': laboratory,
    # }

    return render(request, 'dip/laboratory_result.html', {'result_function': function})


# def laboratory_result(request):
#     posts = Lecture.objects.all()
#
#     context = {
#         # 'posts': posts,
#         'result_function': request.GET['function']
#     }
#
#     return render(request, 'dip/laboratory_result.html', context=context)











# def compiler(request):
#     posts = Lecture.objects.all()
#
#     context = {
#         'posts': posts,
#     }
#
#     return render(request, 'dip/compiler.html', context=context)

# def show_page_parameters_and_inaccuracy(request, laboratory_id):
#     posts = Lecture.objects.all()
#     laboratory = get_object_or_404(Lecture, pk=laboratory_id)
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