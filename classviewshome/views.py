from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import ArticleForm, BookForm
from .models import Article, Book


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
        context['article_books']=Book.objects.filter(article = self.object)
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
