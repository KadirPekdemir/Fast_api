from celery import Celery
from celery.schedules import crontab

app = Celery('my_celery')
app.config_from_object('celery_worker.celery_worker:app')

app.conf.beat_schedule = {
    'send-email-reminders': {
        'task': 'celery_worker.celery_tasks.send_email_task',  # Task definition
        'schedule': crontab(minute=0, hour=0),  # Daily at midnight
    },
    'generate-weekly-reports': {
        'task': 'celery_worker.celery_tasks.generate_weekly_reports_task',  # Task definition
        'schedule': crontab(minute=0, hour=0, day_of_week=0),  # Weekly on Sunday at midnight
    },
}
