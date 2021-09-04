from celery import shared_task
import requests
import logging
from django.db.utils import IntegrityError

from .models import *

logger = logging.getLogger()

CENSUS_URL = 'https://www2.census.gov/programs-surveys/popest/datasets/2010-2020/counties/totals/co-est2020.csv'
SCRATCH_DIR = '/data/scratch'

@shared_task(autoretry_for=(RuntimeError,))
def download_census_data(truncate=False):
    r = requests.get(CENSUS_URL)
    if r.status_code < 200 or r.status_code > 205:
        logger.error("failed to GET url: '%s" - '%d', CENSUS_URL, r.status_code)
        raise RuntimeError("failed to GET url: '%s' - '%d'" % (CENSUS_URL, r.status_code))

    lines = r.text.split('\n')
    #headers = lines[0].split(',')

    if truncate:
        logger.info("truncating table")
        Population.objects.all().delete()
        logger.debug("all objects removed")

    for line in lines[1:]:
        cols = line.split(',')
        if len(cols) > 7 and cols[7] == 'X':
            cols[7] = None
        try:
            Population.objects.create(
                sumlev=cols[0],
                region=cols[1],
                division=cols[2],
                state=cols[3],
                county=cols[4],
                stname=cols[5],
                ctyname=cols[6],
                census2010pop=cols[7],
                estimatesbase2010=cols[8],
                popestimate2010=int(cols[9]),
                popestimate2011=cols[10],
                popestimate2012=cols[11],
                popestimate2013=cols[12],
                popestimate2014=cols[13],
                popestimate2015=cols[14],
                popestimate2016=cols[15],
                popestimate2017=cols[16],
                popestimate2018=cols[17],
                popestimate2019=cols[18],
                popestimate042020=cols[19],
                popestimate2020=cols[20],
            )
        except IntegrityError as exception:
            # duplicate
            logger.error("integrity error(%s): %s", str(exception), line)
            pass
        except ValueError as exception:
#            logger.warning("failed to import line: '%s' - '%s'", line, str(exception))
#            logger.error("failed to import line: '%s' - '%s'", line, str(exception))
            logger.warning("failed to import record: %s", str(exception))
            pass
        except IndexError as exception:
            logger.warning("unexpected number of values: '%s' - '%s'", line, str(exception))
            logger.error("unexpected number of values: '%s' - '%s'", line, str(exception))
    logger.info("import complete")
