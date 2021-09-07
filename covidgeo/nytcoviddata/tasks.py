from celery import shared_task
import requests
import logging
from django.db import transaction
from django.db.utils import IntegrityError

from .models import *

logger = logging.getLogger('root')

NATIONAL_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
STATES_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
COUNTIES_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
SCRATCH_DIR = '/data/scratch'

"""

    The working assumption is that historical data may be corrected. For this
    reason, it makes sense to truncate the tables and re-load the entire
    dataset, unless bulk_update() is used instead.

"""

@shared_task
def import_national(truncate=False):
    r = requests.get(NATIONAL_URL)
    if r.status_code < 200 or r.status_code > 205:
        logger.error("failed to GET url: '%s" - '%d', NATIONAL_URL, r.status_code)
        raise RuntimeError("failed to GET url: '%s' - '%d'" % (NATIONAL_URL, r.status_code))

    lines = r.text.split('\n')

    with transaction.atomic():
        if truncate:
            logger.info("truncating table")
            US.objects.all().delete()
            logger.debug("all objects removed")

        for line in lines[1:]:
            cols = line.split(',')

            try:
                US.objects.create(
                    date=cols[0],
                    cases=cols[1],
                    deaths=cols[2]
                )
            except IntegrityError as exception:
                logger.warning("integrity error(%s): %s", str(exception), line)

        logger.info("import complete")

@shared_task
def import_states(truncate=False):
    r = requests.get(STATES_URL)
    if r.status_code < 200 or r.status_code > 205:
        logger.error("failed to GET url: '%s" - '%d', STATES_URL, r.status_code)
        raise RuntimeError("failed to GET url: '%s' - '%d'" % (STATES_URL, r.status_code))

    lines = r.text.split('\n')

    with transaction.atomic():
        if truncate:
            logger.info("truncating table")
            State.objects.all().delete()
            logger.debug("all objects removed")

        for line in lines[1:]:
            cols = line.split(',')

            try:
                State.objects.create(
                    date=cols[0],
                    state=cols[1],
                    fips=cols[2],
                    cases=cols[3],
                    deaths=cols[4]
                )
            except IntegrityError as exception:
                logger.warning("integrity error(%s): %s", str(exception), line)

        logger.info("import complete")


BATCH_SIZE=50000

# Consider sorting data before inserting to avoid fragmentation of data
@shared_task
def import_counties(truncate=True):
    r = requests.get(COUNTIES_URL)
    if r.status_code < 200 or r.status_code > 205:
        logger.error("failed to GET url: '%s" - '%d', COUNTIES_URL, r.status_code)
        raise RuntimeError("failed to GET url: '%s' - '%d'" % (COUNTIES_URL, r.status_code))

    content_length = len(r.text)
    logger.debug("content length: %d", content_length)

    lines = r.text.split('\n')

    with transaction.atomic():
        if truncate:
            logger.info("truncating table")
            County.objects.all().delete()
            logger.debug("all objects removed")

        total_bytes = content_length - len(lines[0])
        objects = []
        completed_bytes = 0
        completed_rows = 0
        for line in lines[1:]:
            cols = line.split(',')
            completed_bytes += 1+len(line)

            fips = cols[3]
            if fips is None or len(fips) < 1:
                fips = None

            deaths = cols[5]
            if deaths is None or len(deaths) < 1:
                deaths = None

            objects.append(
                County(
                    date=cols[0],
                    county=cols[1],
                    state=cols[2],
                    fips=fips,
                    cases=cols[4],
                    deaths=deaths
                )
            )

            if len(objects) % BATCH_SIZE == 0:
                County.objects.bulk_create(objects, ignore_conflicts=True)
                completed_rows += len(objects)
                objects = []
                logger.debug("completed import of %d rows %.2f%% of total",
                             completed_rows, 100*float(completed_bytes / total_bytes))

        logger.debug("bulk importing %d rows", len(objects))
        County.objects.bulk_create(objects, ignore_conflicts=True)
        completed_rows += len(objects)
        logger.debug("completed import of %d rows %.2f%% of total",
                     completed_rows, 100*float(completed_bytes / total_bytes))

    logger.info("import complete")
