Requirements
- Redis

TO install redis:

    brew install redis

Setup:

    virtualenv venv --no-site-packages -p /usr/local/bin/python3
    venv
    pip install -r requirements.txt
    ./manage.py migrate
    ./manage.py runserver

In other threads you'll need to:

Run redis:

    redis-server

And run the Celeery worker:

    celery -A 'taskmngr' worker -l info


Two things happen:

- A cron scheduled fetch

in fetcher.tasks, a cron function is registered to run every minute:

    @periodic_task(
        run_every=(crontab(minute='*/1')),
        name="download_itunes_data",
        ignore_result=True
    )
    def task_get_chart_data():
        ...

- A URL starts a background task that pauses for 5 seconds and then downloads the file.
