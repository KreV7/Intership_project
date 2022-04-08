import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Intership_project.settings')

app = Celery('Intership_project')
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

# celery beat tasks

app.conf.beat_schedule = {
    'buy_car_showroom_supplier_every_10_minute': {
        'task': 'mainapp.tasks.buy_car_showroom_supplier',
        'schedule': crontab(minute='*/10')
    },
    'buy_car_customer_supplier_every_12_minutes': {
        'task': 'mainapp.tasks.buy_car_customer_supplier',
        'schedule': crontab(minute='*/12')
    }
}
