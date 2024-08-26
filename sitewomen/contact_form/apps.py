from django.apps import AppConfig


class ContactFormConfig(AppConfig):
    verbose_name = 'Почтовые сообщения'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'contact_form'
