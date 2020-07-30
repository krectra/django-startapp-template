from django.apps import AppConfig


class {{ camel_case_app_name }}Config(AppConfig):
    name = '{{ app_name }}'
    
    def ready(self):
        # Add signals import here
        pass
