import os
from dataclasses import dataclass
from typing import Optional

from celery import Celery
from flask import Flask

from .app import bp

# os.environ["CELERY_BROKER"] =  "pyamqp://"
# os.environ["CELERY_BACKEND"] =   "redis://localhost"

@dataclass 
class CeleryConfig:
    broker: Optional[str] = None
    backend: Optional[str] = None

def make_celery(config: CeleryConfig):
    app = Celery(__name__,
                 broker = config.broker, 
                 backend = config.backend,
                 )
    return app 


def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp, url_prefix="") #register preconfig route 

    config = CeleryConfig(broker = os.getenv("CELERY_BROKER"), 
                          backend = os.getenv("CELERY_BACKEND"))

    celery_app = make_celery(config)
    # registers .app.tasks.i to this celery app
    celery_app.set_default() # make default app for all threads 

    return app, celery_app  
