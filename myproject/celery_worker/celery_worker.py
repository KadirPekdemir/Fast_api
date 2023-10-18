from celery import Celery

app = Celery(
    'my_celery',
    broker='pyamqp://guest@localhost//',
    backend='rpc://',
    include=['celery_worker.celery_tasks']  # Celery görevlerini içeren modül adı
)

app.conf.task_routes = {
    'celery_worker.celery_tasks.*': {'queue': 'my_celery'}
}

app.conf.timezone = 'UTC'
