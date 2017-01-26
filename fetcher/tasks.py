import time
from celery.task.schedules import crontab
from celery.decorators import task, periodic_task
from celery.utils.log import get_task_logger

from .utils import get_chart_data

logger = get_task_logger(__name__)


@task
def task_get_chart_data():
    """
    Saves latest image from Flickr
    """
    get_chart_data()
    logger.info("Saved chart data")


@task(name="delayed_get_chart_data")
def delayed_get_chart_data(sleep):
    time.sleep(sleep)
    get_chart_data()
    logger.info("Saved chart data, with a delay")
