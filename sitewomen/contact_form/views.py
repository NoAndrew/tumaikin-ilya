from django.views.generic import CreateView
from .models import Contact
from django.urls import reverse_lazy
from django.core.mail import send_mail
from .forms import ContactForm
from django.views.generic import View
from django.shortcuts import render, redirect

"""
class ContactCreate(CreateView):
    model = Contact
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = ContactForm

    def form_valid(self, form):
        # Формируем сообщение для отправки
        data = form.data
        subject = f'Сообщение с формы от {data["first_name"]} {data["last_name"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)


# Функция отправки сообщения
def email(subject, content):
   send_mail(subject,
      content,
      'отправитель@gmail.com',
      ['получатель1@gmail.com']
   )
"""


class ContactFormView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


