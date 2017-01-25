from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from .utils import get_chart_data

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="download_itunes_data",
    ignore_result=True
)
def task_get_chart_data():
    """
    Saves latest image from Flickr
    """
    get_chart_data()
    logger.info("Saved chart data")