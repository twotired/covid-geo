from celery import shared_task
import logging

from .models import *

logger = logging.getLogger(__name__)

CSV_FILENAME = 'president_county_candidate.csv'
SCRATCH_DIR = '/data/scratch'

@shared_task()
def import_election2020(truncate=False):

    if truncate:
        logger.info("truncating table")
        PresidentCounty2020.objects.all().delete()
        logger.debug("all objects removed")

    with open(SCRATCH_DIR + '/' + CSV_FILENAME, 'r') as fh:
        header = fh.readline()

        for line in fh.readlines():
            cols = line.rstrip().split(',')

            PresidentCounty2020.objects.create(
                state=cols[0],
                county=cols[1],
                candidate=cols[2],
                party=cols[3],
                total_votes=cols[4],
                won=cols[5]
            )

