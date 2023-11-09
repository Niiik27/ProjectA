from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomeTempateView, ArticleListView, ArticleDetailView, ArticleCreateView, BookCreateView, \
    ArticleUpdateView, ArticleDeleteView, UserCreateView,ProfileView,BookUpdateView,BookDeleteView,BookListView,BookDetailView





urlpatterns = [
    path('', HomeTempateView.as_view(), name='home'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
path('books/', BookListView.as_view(), name='book_list'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('books/<int:pk>', BookDetailView.as_view(), name='book_detail'),
    path('update_article/<int:pk>/', ArticleUpdateView.as_view(), name='update_article'),
    path('delete_article/<int:pk>/', ArticleDeleteView.as_view(), name='delete_article'),
    path('create_article/', ArticleCreateView.as_view(), name='create_article'),
    path('create_book/', BookCreateView.as_view(), name='create_book'),
    path('update_book/', BookUpdateView.as_view(), name='update_book'),
    path('delete_book/', BookDeleteView.as_view(), name='delete_book'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('accounts/profile/', ProfileView.as_view(), name='profile')
]
