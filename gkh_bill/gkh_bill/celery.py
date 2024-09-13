import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gkh_bill.settings')
app = Celery('gkh_bill')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
