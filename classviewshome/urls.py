from django.urls import path
from .views import HomeTempateView, ArticleListView, ArticleDetailView, ArticleCreateView, BookCreateView, \
    ArticleUpdateView, ArticleDeleteView

urlpatterns = [
    path('', HomeTempateView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('update_article/<int:pk>/', ArticleUpdateView.as_view(), name='update_article'),
    path('delete_article/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
    path('create_article/', ArticleCreateView.as_view(), name='create_article'),
    path('create_book/', BookCreateView.as_view(), name='create_book'),
]
