from django.apps import AppConfig


class QuickstartConfig(AppConfig):
    name = 'restApp.quickstart'
    # verbose_name = 'A Much Better Name'

    def ready(self):
        import restApp.quickstart.signal