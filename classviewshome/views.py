from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleForm, BookForm, CustomUserCreationForm
from .models import Article, Book, CustomUser


class HomeTempateView(TemplateView):
    template_name = 'classviewshome/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Напиши в адресной строке blog'
        return context


class ArticleListView(ListView):
    model = Article

    def head(self, *args, **kwargs):
        last_book = self.get_queryset().latest("publication_date")
        response = HttpResponse(
            # RFC 1123 date format.
            headers={
                "Last-Modified": last_book.publication_date.strftime(
                    "%a, %d %b %Y %H:%M:%S GMT"
                )
            },
        )
        return response


class ArticleDetailView(DetailView):
    model = Article

    # context_object_name = "q"
    # template_name = 'classviewshome/home.html'
    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context['article_books'] = Book.objects.filter(article=self.object)
        return context


class ArticleUpdateView(UpdateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'

    # context_object_name = "q"
    # template_name = 'classviewshome/home.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['article_books']=Book.objects.filter(article = self.object)
    #     return context


class ArticleDeleteView(DeleteView):
    model = Article
    # form_class = ArticleForm
    success_url = '/articles/'
    # context_object_name = "q"
    # template_name = 'classviewshome/home.html'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['article_books']=Book.objects.filter(article = self.object)
    #     return context


class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    success_url = '/articles/'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    success_url = '/articles/'


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'classviewshome/register.html'

    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.full_name = form.cleaned_data['full_name']
        user.birth_date = form.cleaned_data['birth_date']
        user.save()
        login(self.request, user)
        return super().form_valid(form)

    # class UserLogoutView(LogoutView):
    #     success_url = '/login/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['custom_date'] = 'Напиши в адресной строке blog'
        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'classviewshome/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class BookUpdateView:
    model = Book
    form_class = BookForm
    success_url = '/articles/'


class BookDeleteView:
    model = Book
    success_url = '/articles/'
