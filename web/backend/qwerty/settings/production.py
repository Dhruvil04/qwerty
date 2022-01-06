from .base import *

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

DEBUG = False

# ==============================================================================
# EMAIL CONFIGURATIONS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ==============================================================================
# Celery CONFIGURATIONS
# ==============================================================================

CELERY_BROKER_URL = env.str('CELERY_BROKER')
