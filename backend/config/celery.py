import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'calculate-daily-statistics': {
        'task': 'apps.analytics.tasks.calculate_daily_statistics',
        'schedule': crontab(hour=0, minute=0),
    },
    'detect-anomalies': {
        'task': 'apps.analytics.tasks.detect_anomalies',
        'schedule': crontab(minute=0),  # Every hour
    },
    'check-alerts': {
        'task': 'apps.alerts.tasks.check_alerts',
        'schedule': crontab(minute='*/5'),  # Every 5 minutes
    },
    'calculate-predictions': {
        'task': 'apps.predictions.tasks.calculate_predictions',
        'schedule': crontab(minute='*/15'),  # Every 15 minutes
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
