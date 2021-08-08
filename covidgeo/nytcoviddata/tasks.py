from celery import shared_task
import os
import os.path
import logging

from .models import *

logger = logging.getLogger('root')

HOST = 'ftp2.census.gov'
SCRATCH_DIR = '/data/scratch'

@shared_task
def import_national():
    filename = 'us.csv'
    pass
