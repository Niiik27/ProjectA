from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'text'
        ]


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'article'
        ]


class CustomUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        label="Дата рождения",
        widget=forms.DateInput(attrs={'type':'date','class':'form-input'}),
        help_text="Выберите дату рождения",
        required=False
    )

    class Meta:
        model = CustomUser
        fields = ['full_name', 'birth_date', 'username', 'password1', 'password2']
