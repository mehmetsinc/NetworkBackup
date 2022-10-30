from django.apps import AppConfig


class NetworksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'networks'

    def ready(self):
        from networks.helpers import TaskManager
        TaskManager.sybg()
