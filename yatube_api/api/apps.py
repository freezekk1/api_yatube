"""Django app config for API app."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configuration for API application."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
