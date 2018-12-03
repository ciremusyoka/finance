from django.apps import AppConfig


class LoansappConfig(AppConfig):
    name = 'loansapp'

    def ready(self):
        import loansapp.signals.handlers
        import loansapp.signals.signals