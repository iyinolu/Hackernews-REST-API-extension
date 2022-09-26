from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

    def ready(self):
        # Register scheduler when application is first launched.
        from . import scheduler
        if settings.SCHEDULER_AUTOSTART:
        	scheduler.start()
