from celery import shared_task
import requests
import logging
from django.db.utils import IntegrityError

from .models import *

logger = logging.getLogger('root')

NATIONAL_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv'
STATES_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
COUNTIES_URL = 'https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv'
SCRATCH_DIR = '/data/scratch'

@shared_task
def import_national(truncate=False):
    r = requests.get(NATIONAL_URL)
    if r.status_code < 200 or r.status_code > 205:
        logger.error("failed to GET url: '%s" - '%d', NATIONAL_URL, r.status_code)
        raise RuntimeError("failed to GET url: '%s' - '%d'" % (NATIONAL_URL, r.status_code))

    lines = r.text.split('\n')
    #headers = lines[0].split(',')

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
    #headers = lines[0].split(',')

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

@shared_task
def import_counties(truncate=False):
    r = requests.get(COUNTIES_URL)
    if r.status_code < 200 or r.status_code > 205:
        logger.error("failed to GET url: '%s" - '%d', COUNTIES_URL, r.status_code)
        raise RuntimeError("failed to GET url: '%s' - '%d'" % (COUNTIES_URL, r.status_code))

    lines = r.text.split('\n')
    #headers = lines[0].split(',')

    if truncate:
        logger.info("truncating table")
        County.objects.all().delete()
        logger.debug("all objects removed")

    for line in lines[1:]:
        cols = line.split(',')

        fips = cols[3]
        if fips is None or len(fips) < 1:
            fips = None

        deaths = cols[5]
        if deaths is None or len(deaths) < 1:
            deaths = None

        try:
            County.objects.create(
                date=cols[0],
                county=cols[1],
                state=cols[2],
                fips=fips,
                cases=cols[4],
                deaths=deaths
            )
        except IntegrityError as exception:
            logger.warning("integrity error(%s): %s", str(exception), line)
        except ValueError as exception:
            logger.warning("failed to import record: %s", str(exception))
            pass

    logger.info("import complete")