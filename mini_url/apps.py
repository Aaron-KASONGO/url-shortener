from django.apps import AppConfig


class MiniUrlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mini_url'

    def ready(self):
        import mini_url.signals
