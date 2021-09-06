from celery import shared_task
import os
import os.path
import logging

from ftplib import FTP
from zipfile import ZipFile, BadZipFile

from .models import *
from . import load_states, load_counties, load_contressionaldistricts, load_urbanareas

logger = logging.getLogger()

HOST = 'ftp2.census.gov'
SCRATCH_DIR = '/data/scratch'

def ftp_download(dir, filename, overwrite=False):

    if not overwrite:
        if os.path.isfile(SCRATCH_DIR + '/' + filename):
            logger.debug("already found %s in %s", filename, SCRATCH_DIR)
            return
        else:
            logger.debug("%s not found in %s", filename, SCRATCH_DIR)

    ftp = FTP(HOST)
    ftp.login()
    ftp.cwd(dir)
    with open(SCRATCH_DIR + '/' + filename, 'wb') as fp:
        ftp.retrbinary('RETR ' + filename, fp.write)
    logger.info("finished downloading %s", filename)

    ftp.quit()


def download_shapes(ftp_dir, zipfile, shapefile, model, import_func, overwrite=False):
    extract_dir = SCRATCH_DIR + '/' + 'extracted'

    try:
        os.makedirs(extract_dir)
    except FileExistsError:
        logger.debug("dir '%s' already existed", extract_dir)

    ftp_download(ftp_dir, zipfile, overwrite)

    # extract
    try:
        with ZipFile(SCRATCH_DIR + '/' + zipfile, 'r') as zip_fd:
            zip_fd.extractall(extract_dir)
    except BadZipFile:
        logger.warn("found bad zip file - downloading again")
        ftp_download(ftp_dir, zipfile, True)
        with ZipFile(SCRATCH_DIR + '/' + zipfile, 'r') as zip_fd:
            zip_fd.extractall(extract_dir)

    logger.debug("finished extracting %s/%s into %s", SCRATCH_DIR, zipfile,
                extract_dir)

    # empty table
    model.objects.all().delete()
    logger.debug("emptied table %s", model.objects.model._meta.db_table)

    # import
    import_func.run(extract_dir + '/' + shapefile)
    logger.debug("populated table %s", model.objects.model._meta.db_table)


@shared_task
def download_states(overwrite=False):
    download_shapes('/geo/tiger/TIGER2020/STATE', 'tl_2020_us_state.zip',
                    'tl_2020_us_state.shp', State, load_states, overwrite)


@shared_task
def download_contressionaldistricts(overwrite=False):
    download_shapes('/geo/tiger/TIGER2020/CD', 'tl_2020_us_cd116.zip',
                    'tl_2020_us_cd116.shp', CongressionalDistrict,
                    load_contressionaldistricts, overwrite)


@shared_task
def download_urbanareas(overwrite=False):
    download_shapes('/geo/tiger/TIGER2020/UAC', 'tl_2020_us_uac10.zip',
                    'tl_2020_us_uac10.shp', UrbanArea, load_urbanareas,
                    overwrite)


@shared_task
def download_counties(overwrite=False):
    download_shapes('/geo/tiger/TIGER2020/COUNTY', 'tl_2020_us_county.zip',
                    'tl_2020_us_county.shp', County, load_counties, overwrite)
