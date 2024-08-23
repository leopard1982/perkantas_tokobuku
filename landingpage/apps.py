from django.apps import AppConfig
import os
from django.conf import settings
import shutil


class LandingpageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'landingpage'

    def ready(self) -> None:
        return super().ready()
