import time

from celery import shared_task


@shared_task(bind=True)
def i(self, x):
    time.sleep(5)
    return x
