# Joke_Project_Celery_and_Channels

git clone "url"

pip install -r requirements.txt
cd project
first start Django Server :- Python manage.py runserver
than,
    start celery beat
        :- celery -A project/main-project-name beat -l INFO
    start worker
        :- celery -A project worker --pool=solo -l info
""
i hope all is good
""
