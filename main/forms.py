# Импортируем модуль forms
from django import forms


# Создаём форму обратной связи
# Объявим класс
class ContactForm(forms.Form):
    name = forms.CharField(  # CharField - проверит корректность веденного значение строка или нет
        min_length=2,  # Указываем минимальное количество символов
        widget=forms.TextInput(
            attrs={'placeholder': 'Ваше имя'}
        )
    )
    email = forms.EmailField(  # EmailField - проверит коррекность веденного имейла самостоятельно

        widget=forms.EmailInput(
            attrs={'placeholder': 'E-mail'}
        )
    )
    massage = forms.CharField(
        min_length=20,
        widget=forms.Textarea(
            attrs={'placeholder': 'Сообщение'}
        )
    )

    fone = forms.CharField(
        min_length=20,
        widget=forms.TextInput(
            attrs={'placeholder': 'Номер телефона'}
        )
    )

